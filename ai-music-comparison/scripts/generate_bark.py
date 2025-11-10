#!/usr/bin/env python3
"""
Bark Vocal Generation Script

Generates vocal segments for AI music comparison experiment.
Bark Model: https://github.com/suno-ai/bark

IMPORTANT: Activate venv-bark before running:
  source venv-bark/bin/activate
  python scripts/generate_bark.py

Segments:
  - Segment 10: Chorus vocals (5s target, "Susurra Conmigo")
  - Segment 18: Verse vocals (5s target, "Caos y Suerte")

Constraints:
  - Bark hard limit: ~13 seconds or 24 words
  - Our segments: 5s each (well within limit)
"""

import os
import sys
from pathlib import Path
import numpy as np
from scipy.io.wavfile import write as write_wav

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Set cache directory to project-local (avoid permission issues with ~/.cache)
CACHE_DIR = PROJECT_ROOT / ".cache" / "bark"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
os.environ['XDG_CACHE_HOME'] = str(PROJECT_ROOT / ".cache")
os.environ['SUNO_USE_SMALL_MODELS'] = '1'  # Use small models to save memory
os.environ['SUNO_OFFLOAD_CPU'] = '1'  # Offload to CPU if needed

# Fix PyTorch 2.6+ weights_only breaking change
# Bark uses old checkpoint format incompatible with weights_only=True
# This is safe for Bark's official checkpoints from Suno AI
import torch

# Monkey-patch torch.load to use weights_only=False (required for Bark compatibility)
_original_torch_load = torch.load
def _patched_torch_load(*args, **kwargs):
    kwargs.setdefault('weights_only', False)
    return _original_torch_load(*args, **kwargs)
torch.load = _patched_torch_load

# Check we're in the right venv
try:
    from bark import SAMPLE_RATE, generate_audio, preload_models
    from bark.generation import SUPPORTED_LANGS
except ImportError:
    print("❌ Error: Bark not installed")
    print("Please activate venv-bark:")
    print("  source venv-bark/bin/activate")
    sys.exit(1)

# Output directory
OUTPUT_DIR = PROJECT_ROOT / "results" / "local_models"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_segment_10_chorus():
    """
    Segment 10: Chorus (Vocal)

    Suno style tags from suno_test_segments.md lines 38-44:
    - Latin trap / reggaetón / electronic milonga fusion
    - Tempo: mid-slow urban flow (120 BPM)
    - Mood: mystical + empowered + emotional
    - Voice: smooth male lead + female harmonies + layered vocals
    - Emotional intensity - peak chorus energy
    """

    print("\n=== Generating Segment 10: Chorus (Susurra Conmigo) ===")

    # Bark format with Suno style tags translated
    prompt = """[MAN, singing Latin trap reggaeton electronic milonga fusion style, 120 BPM mid-slow urban flow, mystical empowered emotional mood, smooth male lead with female harmonies and layered vocals, peak chorus energy]
♪ We whisper — (susurra conmigo)
♪ Whisper del futuro, amor y código
♪ We whisper — (susurra conmigo)
♪ Entre el alma y la data, we make it musical ♪
[soft vocal echo with reverb: susurra... susurra...]"""

    print(f"Prompt: {prompt}")
    print("Generating audio (this may take 30-60 seconds)...")

    try:
        audio_array = generate_audio(prompt)

        # Save to WAV
        output_path = OUTPUT_DIR / "bark_segment10_chorus.wav"
        write_wav(output_path, SAMPLE_RATE, audio_array)

        duration = len(audio_array) / SAMPLE_RATE
        print(f"✅ Generated: {output_path}")
        print(f"   Duration: {duration:.2f}s")
        print(f"   Sample rate: {SAMPLE_RATE} Hz")

        return output_path

    except Exception as e:
        print(f"❌ Error generating segment 10: {e}")
        return None


def generate_segment_18_verse():
    """
    Segment 18: Verse (Vocal)

    Suno style tags from suno_test_segments.md lines 68-73:
    - Latin trap / reggaetón / electronic milonga fusion
    - Tempo: mid-slow urban flow (122 BPM)
    - Mood: playful + empowered + reflective
    - Voice: smooth male lead with natural tone variation
    - Upbeat verse with clear rhythm
    """

    print("\n=== Generating Segment 18: Verse (Caos y Suerte) ===")

    # Bark format with Suno style tags translated
    prompt = """[MAN, singing Latin trap reggaeton electronic milonga fusion style, 122 BPM mid-slow urban flow, playful empowered reflective mood, smooth male lead with natural tone variation, upbeat verse with clear rhythm]
♪ We laugh at the chaos, we play con la suerte,
♪ Dreams synthetic but hearts still imperfect.
♪ Mientras el mundo corre, nosotros escuchamos,
♪ La máquina escribe, pero humanos cantamos. ♪
[background whisper vocals: susurra, susurra...]"""

    print(f"Prompt: {prompt}")
    print("Generating audio (this may take 30-60 seconds)...")

    try:
        audio_array = generate_audio(prompt)

        # Save to WAV
        output_path = OUTPUT_DIR / "bark_segment18_verse.wav"
        write_wav(output_path, SAMPLE_RATE, audio_array)

        duration = len(audio_array) / SAMPLE_RATE
        print(f"✅ Generated: {output_path}")
        print(f"   Duration: {duration:.2f}s")
        print(f"   Sample rate: {SAMPLE_RATE} Hz")

        return output_path

    except Exception as e:
        print(f"❌ Error generating segment 18: {e}")
        return None


def main():
    """Generate all Bark vocal segments"""

    print("=" * 60)
    print("Bark Vocal Generation - AI Music Comparison")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Bark sample rate: {SAMPLE_RATE} Hz")

    # Preload models for faster generation
    print("\n⏳ Preloading Bark models (this may take 1-2 minutes)...")
    try:
        preload_models()
        print("✅ Models loaded")
    except Exception as e:
        print(f"⚠️  Warning: Could not preload models: {e}")
        print("   Continuing anyway (models will load on first generation)")

    # Generate segments
    results = []

    seg10 = generate_segment_10_chorus()
    if seg10:
        results.append(("Segment 10 (Chorus)", seg10))

    seg18 = generate_segment_18_verse()
    if seg18:
        results.append(("Segment 18 (Verse)", seg18))

    # Summary
    print("\n" + "=" * 60)
    print("Generation Complete")
    print("=" * 60)

    if results:
        print(f"✅ Generated {len(results)}/2 segments:")
        for name, path in results:
            print(f"   - {name}: {path.name}")
    else:
        print("❌ No segments generated successfully")
        return 1

    print("\nNext steps:")
    print("  1. Listen to generated vocals")
    print("  2. Compare with baseline: data/baseline/suno_segment*.wav")
    print("  3. Run librosa analysis (Phase 4)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
