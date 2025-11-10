#!/usr/bin/env python3
"""
Audio Comparison Script (librosa)

Compares Suno baseline vs Bark vocal segments using audio feature extraction.

IMPORTANT: Activate venv-analysis before running:
  source venv-analysis/bin/activate
  python scripts/compare_audio.py

Comparison pairs:
  - Segment 10: suno_segment10_chorus.wav vs bark_segment10_chorus.wav
  - Segment 18: suno_segment18_verse.wav vs bark_segment18_verse.wav

Features extracted:
  - Tempo (BPM)
  - Spectral centroid (brightness)
  - MFCCs (timbre/vocal quality)
  - Chroma (harmonic content)
  - Zero-crossing rate (noisiness)
  - RMS energy (loudness)
"""

import sys
from pathlib import Path
import numpy as np
import json

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Check we're in the right venv
try:
    import librosa
    import librosa.display
except ImportError:
    print("❌ Error: librosa not installed")
    print("Please activate venv-analysis:")
    print("  source venv-analysis/bin/activate")
    sys.exit(1)

# Paths
BASELINE_DIR = PROJECT_ROOT / "data" / "baseline"
LOCAL_MODELS_DIR = PROJECT_ROOT / "results" / "local_models"
OUTPUT_DIR = PROJECT_ROOT / "results" / "analysis"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def extract_features(audio_path: Path) -> dict:
    """
    Extract audio features from WAV file using librosa.

    Returns dict with:
      - tempo: BPM estimate
      - spectral_centroid: Mean brightness (Hz)
      - mfcc: Mean MFCCs (timbre descriptor, 13 coefficients)
      - chroma: Mean chroma (harmonic content, 12 pitch classes)
      - zcr: Mean zero-crossing rate (noisiness)
      - rms_energy: Mean RMS energy (loudness)
      - duration: Audio length in seconds
      - sample_rate: Sample rate in Hz
    """

    print(f"  Loading: {audio_path.name}")

    # Load audio
    y, sr = librosa.load(audio_path, sr=None)
    duration = librosa.get_duration(y=y, sr=sr)

    print(f"    Duration: {duration:.2f}s, Sample rate: {sr} Hz")

    # Tempo estimation
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    # Spectral centroid (brightness)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    spectral_centroid_mean = float(np.mean(spectral_centroid))

    # MFCCs (timbre)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = mfccs.mean(axis=1).tolist()  # Mean across time for each coefficient

    # Chroma (harmonic content)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma_mean = chroma.mean(axis=1).tolist()  # Mean across time for each pitch class

    # Zero-crossing rate (noisiness)
    zcr = librosa.feature.zero_crossing_rate(y)
    zcr_mean = float(np.mean(zcr))

    # RMS energy (loudness)
    rms = librosa.feature.rms(y=y)
    rms_mean = float(np.mean(rms))

    return {
        "tempo": float(tempo),
        "spectral_centroid_hz": spectral_centroid_mean,
        "mfcc_mean": mfcc_mean,
        "chroma_mean": chroma_mean,
        "zcr_mean": zcr_mean,
        "rms_energy": rms_mean,
        "duration_s": duration,
        "sample_rate": sr
    }


def compare_segments(segment_num: int, segment_name: str, suno_file: str, bark_file: str) -> dict:
    """
    Compare Suno baseline vs Bark for a single segment.

    Returns comparison dict with:
      - segment_info: name, number
      - suno_features: extracted features
      - bark_features: extracted features
      - differences: calculated deltas
    """

    print(f"\n=== Segment {segment_num}: {segment_name} ===")

    suno_path = BASELINE_DIR / suno_file
    bark_path = LOCAL_MODELS_DIR / bark_file

    # Check files exist
    if not suno_path.exists():
        print(f"❌ Suno baseline not found: {suno_path}")
        return None

    if not bark_path.exists():
        print(f"❌ Bark output not found: {bark_path}")
        return None

    # Extract features
    print("Extracting features from Suno baseline:")
    suno_features = extract_features(suno_path)

    print("Extracting features from Bark output:")
    bark_features = extract_features(bark_path)

    # Calculate differences
    tempo_diff = bark_features["tempo"] - suno_features["tempo"]
    tempo_diff_pct = (tempo_diff / suno_features["tempo"]) * 100 if suno_features["tempo"] > 0 else 0

    spectral_diff = bark_features["spectral_centroid_hz"] - suno_features["spectral_centroid_hz"]
    spectral_diff_pct = (spectral_diff / suno_features["spectral_centroid_hz"]) * 100 if suno_features["spectral_centroid_hz"] > 0 else 0

    duration_diff = bark_features["duration_s"] - suno_features["duration_s"]

    # MFCCs similarity (cosine similarity)
    mfcc_similarity = float(np.dot(suno_features["mfcc_mean"], bark_features["mfcc_mean"]) /
                           (np.linalg.norm(suno_features["mfcc_mean"]) * np.linalg.norm(bark_features["mfcc_mean"])))

    # Chroma similarity (cosine similarity)
    chroma_similarity = float(np.dot(suno_features["chroma_mean"], bark_features["chroma_mean"]) /
                             (np.linalg.norm(suno_features["chroma_mean"]) * np.linalg.norm(bark_features["chroma_mean"])))

    differences = {
        "tempo_diff_bpm": tempo_diff,
        "tempo_diff_pct": tempo_diff_pct,
        "spectral_centroid_diff_hz": spectral_diff,
        "spectral_centroid_diff_pct": spectral_diff_pct,
        "duration_diff_s": duration_diff,
        "mfcc_similarity": mfcc_similarity,  # 1.0 = identical, 0.0 = completely different
        "chroma_similarity": chroma_similarity,  # 1.0 = identical, 0.0 = completely different
        "zcr_diff": bark_features["zcr_mean"] - suno_features["zcr_mean"],
        "rms_energy_diff": bark_features["rms_energy"] - suno_features["rms_energy"]
    }

    return {
        "segment_info": {
            "number": segment_num,
            "name": segment_name
        },
        "suno_features": suno_features,
        "bark_features": bark_features,
        "differences": differences
    }


def generate_summary(results: list) -> str:
    """
    Generate human-readable summary of comparison results.
    """

    summary_lines = []
    summary_lines.append("=" * 60)
    summary_lines.append("Audio Comparison: Suno Baseline vs Bark Vocals")
    summary_lines.append("=" * 60)
    summary_lines.append("")

    for result in results:
        if result is None:
            continue

        info = result["segment_info"]
        diff = result["differences"]
        suno = result["suno_features"]
        bark = result["bark_features"]

        summary_lines.append(f"## Segment {info['number']}: {info['name']}")
        summary_lines.append("")

        # Duration
        summary_lines.append(f"**Duration**:")
        summary_lines.append(f"  - Suno: {suno['duration_s']:.2f}s")
        summary_lines.append(f"  - Bark: {bark['duration_s']:.2f}s")
        summary_lines.append(f"  - Difference: {diff['duration_diff_s']:+.2f}s")
        summary_lines.append("")

        # Tempo
        summary_lines.append(f"**Tempo**:")
        summary_lines.append(f"  - Suno: {suno['tempo']:.1f} BPM")
        summary_lines.append(f"  - Bark: {bark['tempo']:.1f} BPM")
        summary_lines.append(f"  - Difference: {diff['tempo_diff_bpm']:+.1f} BPM ({diff['tempo_diff_pct']:+.1f}%)")
        summary_lines.append("")

        # Spectral centroid (brightness)
        summary_lines.append(f"**Spectral Centroid (Brightness)**:")
        summary_lines.append(f"  - Suno: {suno['spectral_centroid_hz']:.0f} Hz")
        summary_lines.append(f"  - Bark: {bark['spectral_centroid_hz']:.0f} Hz")
        summary_lines.append(f"  - Difference: {diff['spectral_centroid_diff_hz']:+.0f} Hz ({diff['spectral_centroid_diff_pct']:+.1f}%)")
        summary_lines.append("")

        # Timbre similarity (MFCCs)
        summary_lines.append(f"**Timbre Similarity (MFCC cosine similarity)**:")
        summary_lines.append(f"  - Score: {diff['mfcc_similarity']:.3f} (1.0 = identical, 0.0 = completely different)")
        summary_lines.append("")

        # Harmonic similarity (Chroma)
        summary_lines.append(f"**Harmonic Similarity (Chroma cosine similarity)**:")
        summary_lines.append(f"  - Score: {diff['chroma_similarity']:.3f} (1.0 = identical, 0.0 = completely different)")
        summary_lines.append("")

        # Energy
        summary_lines.append(f"**RMS Energy (Loudness)**:")
        summary_lines.append(f"  - Suno: {suno['rms_energy']:.4f}")
        summary_lines.append(f"  - Bark: {bark['rms_energy']:.4f}")
        summary_lines.append(f"  - Difference: {diff['rms_energy_diff']:+.4f}")
        summary_lines.append("")

        # Noisiness
        summary_lines.append(f"**Zero-Crossing Rate (Noisiness)**:")
        summary_lines.append(f"  - Suno: {suno['zcr_mean']:.4f}")
        summary_lines.append(f"  - Bark: {bark['zcr_mean']:.4f}")
        summary_lines.append(f"  - Difference: {diff['zcr_diff']:+.4f}")
        summary_lines.append("")
        summary_lines.append("---")
        summary_lines.append("")

    summary_lines.append("## Key Findings")
    summary_lines.append("")
    summary_lines.append("### Similarities")
    summary_lines.append("- (To be filled based on data)")
    summary_lines.append("")
    summary_lines.append("### Differences")
    summary_lines.append("- (To be filled based on data)")
    summary_lines.append("")
    summary_lines.append("### Qualitative Observations")
    summary_lines.append("- (Listen to audio files for subjective assessment)")
    summary_lines.append("")

    return "\n".join(summary_lines)


def main():
    """
    Run audio comparison for all segment pairs.
    """

    print("=" * 60)
    print("Audio Comparison: Suno Baseline vs Bark Vocals")
    print("=" * 60)
    print(f"Baseline directory: {BASELINE_DIR}")
    print(f"Bark outputs: {LOCAL_MODELS_DIR}")
    print(f"Results directory: {OUTPUT_DIR}")
    print("")

    # Define comparison pairs
    comparisons = [
        {
            "segment_num": 10,
            "segment_name": "Chorus (Susurra Conmigo)",
            "suno_file": "suno_segment10_chorus.wav",
            "bark_file": "bark_segment10_chorus.wav"
        },
        {
            "segment_num": 18,
            "segment_name": "Verse (Caos y Suerte)",
            "suno_file": "suno_segment18_verse.wav",
            "bark_file": "bark_segment18_verse.wav"
        }
    ]

    # Run comparisons
    results = []
    for comp in comparisons:
        result = compare_segments(**comp)
        if result:
            results.append(result)

    # Save JSON results
    json_output = OUTPUT_DIR / "comparison_results.json"
    with open(json_output, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n✅ JSON results saved: {json_output}")

    # Generate and save human-readable summary
    summary = generate_summary(results)
    summary_output = OUTPUT_DIR / "comparison_results.md"
    with open(summary_output, 'w') as f:
        f.write(summary)

    print(f"✅ Summary saved: {summary_output}")

    # Print summary to console
    print("\n" + summary)

    print("\nNext steps:")
    print("  1. Review comparison_results.json for detailed metrics")
    print("  2. Listen to audio pairs for qualitative assessment")
    print("  3. Update comparison_results.md with key findings")
    print("  4. Prepare presentation materials (Phase 5)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
