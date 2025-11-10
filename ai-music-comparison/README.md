# AI Music Generation Comparison: Suno vs Open-Source Models

**Research Project**: Comparing commercial AI music generation (Suno.ai) with open-source alternatives (Bark, Stable Audio, MusicGen)

**Timeline**: 4 days (November 2025)
**Presentation**: AI Whisperers Buenos Aires (Tuesday evening)
**Approach**: Journey over perfection ❤️+🌀=🌈

---

## TL;DR

**Question**: Can local, open-source AI models generate music comparable to commercial services like Suno.ai?

**Answer**: **Partially**. Bark (vocals) works but has significant quality gaps. Stable Audio and MusicGen hit technical blockers.

**Key Finding**: Commercial models (Suno) maintain substantial lead over open-source alternatives. Local generation is viable for experimentation, not production.

---

## What We Built

### Experiment Scope
- **Baseline**: 3 segments from Suno.ai-generated song "Whispers del Futuro" (Latin trap/reggaetón/electronic milonga fusion)
- **Local Models Attempted**: Bark (vocals), Stable Audio (instrumental), MusicGen (instrumental)
- **Analysis**: librosa audio feature extraction and comparison

### Results
- ✅ **Bark** (vocals): 2/2 segments generated successfully
- ❌ **Stable Audio** (instrumental): Recursion errors on both MPS and CPU
- ❌ **MusicGen** (instrumental): PyAV/ffmpeg dependency incompatibility

**Final Deliverable**: 2-way comparison (Suno vs Bark vocals) with quantitative metrics

---

## Key Findings

### What Bark Got Right ✅

| Metric | Result | Interpretation |
|--------|--------|----------------|
| **Timbre Similarity** | 94% (0.934-0.940 MFCC match) | Successfully captures similar vocal characteristics |
| **Tempo Tracking** | Within 2-7% (117-128 BPM) | Basic rhythm matching works |
| **Harmonic Coherence (Chorus)** | 91% (0.910 Chroma match) | Follows melody well in emotional contexts |

### Where Bark Struggled ❌

| Limitation | Impact | Numbers |
|-----------|--------|---------|
| **Duration Constraint** | Can't recreate full segments | ~14s max (vs 20-47s Suno segments) |
| **Noisiness** | Substantial audio quality gap | 4x more artifacts (319% increase in chorus) |
| **Verse Melodic Accuracy** | Struggles with conversational content | 45% harmonic match (vs 91% in chorus) |
| **Loudness Inconsistency** | Lacks nuanced dynamics | Verse 420% louder than Suno |

---

## Technical Challenges

### Successful: Bark
- **Setup**: Python 3.11, PyTorch 2.9.0, CPU-only (M4 Max)
- **Performance**: 30-60s generation time per 14s segment
- **Fixes Applied**:
  - PyTorch 2.6+ `weights_only` breaking change (monkey-patched)
  - Cache permission issues (XDG_CACHE_HOME override)
  - Suno style tag translation to Bark format

### Blocked: Stable Audio
- **Issue**: `maximum recursion depth exceeded` on both MPS and CPU
- **Root Cause**: Model compatibility bug (not configuration)
- **Attempts**: float16, float32, reduced inference steps - all failed

### Blocked: MusicGen
- **Issue**: PyAV v11.0.0 incompatible with system ffmpeg 8.x
- **Attempts**:
  1. venv (PyAV build fails on ffmpeg API mismatch)
  2. Docker with Debian Bullseye (ffmpeg 4.x too old)
  3. Docker with Debian Bookworm (PyAV still fails)
- **Root Cause**: audiocraft hard-pins `av==11.0.0`, which uses ffmpeg 6.x API

---

## Repository Structure

```
ai-music-comparison/
├── README.md                           # This file
├── PRESENTATION_SUMMARY.md             # 12-minute talk notes
├── PRESENTATION_CHECKLIST.md           # Day-of setup guide
├── PRESENTATION_OUTLINE.md             # Detailed outline
├── PLAN.md                             # Project roadmap + status
├── PHASE3_FINAL_STATUS.md              # Technical deep-dive
├── data/
│   ├── baseline/                       # Suno.ai originals
│   │   ├── suno_segment10_chorus.wav   # 46.92s, 48kHz
│   │   ├── suno_segment18_verse.wav    # 19.60s, 48kHz
│   │   └── SONG.md                     # Full lyrics + metadata
│   └── segments/
│       └── suno_test_segments.md       # Test segment definitions
├── results/
│   ├── local_models/                   # Bark outputs
│   │   ├── bark_segment10_chorus.wav   # 14.36s, 24kHz
│   │   └── bark_segment18_verse.wav    # 13.91s, 24kHz
│   └── analysis/                       # librosa comparison
│       ├── comparison_results.md       # Human-readable findings
│       └── comparison_results.json     # Raw metrics
├── scripts/
│   ├── generate_bark.py                # Bark generation script
│   ├── compare_audio.py                # librosa analysis script
│   ├── setup_bark.sh                   # Bark environment setup
│   └── setup_analysis.sh               # Analysis environment setup
├── requirements-bark.txt               # Bark dependencies
└── requirements-analysis.txt           # Analysis dependencies
```

---

## Quick Start

### Listen to Comparisons

**Suno Baseline** (commercial quality):
- `data/baseline/suno_segment10_chorus.wav` - "Susurra Conmigo" chorus
- `data/baseline/suno_segment18_verse.wav` - "Caos y Suerte" verse

**Bark Output** (open-source attempt):
- `results/local_models/bark_segment10_chorus.wav` - Bark chorus
- `results/local_models/bark_segment18_verse.wav` - Bark verse

Play first 10 seconds of each pair for side-by-side comparison.

### Run Bark Generation

```bash
# Setup environment
./scripts/setup_bark.sh

# Activate venv
source venv-bark/bin/activate

# Generate vocals
python scripts/generate_bark.py
```

### Run Analysis

```bash
# Setup environment
./scripts/setup_analysis.sh

# Activate venv
source venv-analysis/bin/activate

# Compare audio
python scripts/compare_audio.py
```

---

## Key Metrics

| Metric | Segment 10 (Chorus) | Segment 18 (Verse) |
|--------|---------------------|-------------------|
| **Duration** | Suno: 46.92s / Bark: 14.36s | Suno: 19.60s / Bark: 13.91s |
| **Tempo** | Suno: 119.7 BPM / Bark: 127.8 BPM (+6.8%) | Suno: 119.7 BPM / Bark: 117.2 BPM (-2.1%) |
| **Timbre (MFCC)** | 0.934 similarity (93.4% match) | 0.940 similarity (94.0% match) |
| **Harmony (Chroma)** | 0.910 similarity (91.0% match) | 0.447 similarity (44.7% match) |
| **Noisiness (ZCR)** | +319% increase | +32% increase |
| **Loudness (RMS)** | +30% | +420% |

---

## Lessons Learned

### Technical
1. **CPU-only is viable**: Bark proves local generation works without GPU (30-60s per 14s segment)
2. **Quality gap is real**: 94% timbre similarity but 4x noisier = unusable for production
3. **Dependency hell is real**: PyTorch versions, ffmpeg APIs, PyAV incompatibilities
4. **Model maturity varies**: Not all "open" models are deployment-ready

### Process
1. **MVP flexibility essential**: Adjusted from 3-way to 2-way comparison when models failed
2. **Measurement validates intuition**: librosa quantifies the quality gap objectively
3. **Journey over perfection**: Honest about failures, focused on learnings

---

## Presentation Materials

**Primary Documents**:
- `PRESENTATION_SUMMARY.md` - Concise 12-minute talk notes
- `PRESENTATION_CHECKLIST.md` - Pre-talk setup guide
- `results/analysis/comparison_results.md` - Detailed metrics

**For Q&A**:
- `PHASE3_FINAL_STATUS.md` - Technical deep-dive on blockers
- `PLAN.md` - Full project timeline and decisions

---

## Hardware & Software

**System**: M4 Max MacBook Pro, 128GB RAM, 16 cores
**Models Tested**:
- Bark (Suno AI) - MIT license, CPU-only
- Stable Audio Open (Stability AI) - Gated HuggingFace model
- MusicGen (Meta AudioCraft) - Facebook Research

**Dependencies**:
- Python 3.11
- PyTorch 2.9.0 (Bark), 2.1.0 (MusicGen)
- librosa 0.11.0 (analysis)

---

## Future Work

**MusicGen**:
- Build custom PyAV wheel for ffmpeg 8.x
- Or fork audiocraft to support newer PyAV versions
- Or use Docker with proper cross-compilation for ffmpeg 6.x

**Bark Improvements**:
- Implement chunking for longer audio (>14s)
- Fine-tuning experiments with music-specific data
- Multi-speaker/harmony generation

**Stable Audio**:
- Wait for upstream bug fix
- Or test alternative Stability AI models

---

## Citation

If you use this work, please cite:

```
AI Music Generation Comparison: Suno vs Open-Source Models
Research by Lee (AI Whisperers Buenos Aires, November 2025)
https://github.com/[your-username]/ai-music-context
```

---

## License

**Audio Files**: Original Suno.ai generation (see data/baseline/SONG.md for attribution)
**Code**: MIT License
**Documentation**: CC BY 4.0

---

## Acknowledgments

- **Suno AI**: Bark model (MIT license) and baseline music generation
- **Stability AI**: Stable Audio Open model (attempted)
- **Meta AI**: MusicGen/AudioCraft (attempted)
- **AI Whisperers Buenos Aires**: Community and presentation opportunity

---

**Status**: ✅ Complete - Ready for presentation
**Timeline**: 4 days (Sat 1pm → Sun 8pm)
**Approach**: ❤️+🌀=🌈 (journey over perfection)
