# AI Music Generation Comparison - Presentation Summary

**Event**: AI Whisperers Buenos Aires
**Date**: Tuesday evening
**Presenter**: Lee (twin)

---

## TL;DR (30 seconds)

**Question**: Can local AI models generate music comparable to commercial services like Suno.ai?

**Answer**: **Partially**. Bark (open-source vocals) works but has significant quality gaps. Stable Audio and MusicGen hit technical blockers. Demonstrates the current state of open-source AI music generation.

**Key Insight**: Commercial models (Suno) maintain substantial lead over open-source alternatives. Local generation is viable for experimentation, not production.

---

## What We Built (2 min)

### Scope
- **Baseline**: 3 Suno.ai segments from "Whispers del Futuro" (Latin trap/reggaetón/electronic milonga fusion)
- **Local Models**: Attempted 3 (Bark, Stable Audio, MusicGen)
- **Analysis**: librosa audio feature extraction + comparison

### Results
- ✅ **Bark** (vocals): 2/2 segments generated successfully
- ❌ **Stable Audio** (instrumental): Recursion errors on both MPS and CPU
- ❌ **MusicGen** (instrumental): PyAV/ffmpeg dependency incompatibility (even in Docker)

**Final Deliverable**: 2-way comparison (Suno vs Bark vocals) with quantitative metrics

---

## Key Findings (3 min)

### What Bark Got Right ✅

**Vocal Timbre** (94% similarity):
- Segment 10 (Chorus): 0.934 MFCC match
- Segment 18 (Verse): 0.940 MFCC match
- **Meaning**: Bark successfully captures similar voice characteristics to Suno

**Tempo Tracking**:
- Within 2-7% of Suno tempo (117-128 BPM)
- **Meaning**: Basic rhythm matching works

**Harmonic Coherence (Chorus)** (91% similarity):
- Segment 10: 0.910 Chroma match
- **Meaning**: Bark follows melody well in emotional/chorus contexts

### Where Bark Struggled ❌

**Duration Constraint** (hard limit):
- Suno Segment 10: 46.92s → Bark: 14.36s (-69%)
- Suno Segment 18: 19.60s → Bark: 13.91s (-29%)
- **Meaning**: Bark has ~13-15 second generation limit, can't recreate full segments

**Noisiness/Artifacts** (4x worse):
- Segment 10: +319% noise increase vs Suno
- **Meaning**: Substantial audio quality gap, audible artifacts

**Melodic Accuracy (Verse)** (45% match):
- Segment 18: 0.447 Chroma similarity (LOW)
- **Meaning**: Struggles with conversational/verse content (chorus works better)

**Loudness Inconsistency**:
- Segment 10: +30% louder
- Segment 18: +420% louder
- **Meaning**: Lacks nuanced dynamics, overcompensates in verse

---

## Technical Challenges (2 min)

### Successful: Bark
- **Setup**: Python 3.11, PyTorch 2.9.0, project-local cache
- **Fixes Applied**:
  - PyTorch 2.6+ `weights_only` breaking change (monkey-patched)
  - Cache permission issues (XDG_CACHE_HOME override)
  - Suno style tag translation to Bark format
- **Performance**: 30-60s generation time per 14s segment (CPU-only, M4 Max)

### Blocked: Stable Audio
- **Issue**: `maximum recursion depth exceeded` on both MPS and CPU
- **Root Cause**: Model compatibility bug (not configuration)
- **Attempts**: float16, float32, reduced inference steps - all failed
- **Decision**: Marked as non-functional for MVP

### Blocked: MusicGen
- **Issue**: PyAV v11.0.0 incompatible with system ffmpeg 8.x
- **Attempts**:
  1. venv: av 11.0.0 requires `AV_OPT_TYPE_CHANNEL_LAYOUT` (ffmpeg 6.x API)
  2. Docker (Debian Bullseye): ffmpeg 4.x (too old)
  3. Docker (Debian Bookworm): PyAV still fails to build
- **Root Cause**: audiocraft hard-pins `av==11.0.0`, which uses old ffmpeg 6.x API
- **Decision**: Deferred to future work (requires custom PyAV build or audiocraft fork)

---

## Lessons Learned (2 min)

### Technical Insights

1. **Model Maturity Varies**:
   - Bark: Functional but limited (TTS-adapted, not music production)
   - Stable Audio: Gated but broken (recursion error)
   - MusicGen: Requires complex dependency isolation

2. **CPU-Only is Viable**:
   - Bark proves local generation works without GPU
   - 30-60 seconds per 14-second segment (acceptable for experimentation)

3. **Quality Gap is Real**:
   - 94% timbre similarity sounds impressive...
   - ...but 4x noisier + duration limits = unusable for production
   - Commercial models (Suno) have massive lead

4. **Dependency Hell is Real**:
   - PyTorch version conflicts (2.1.0 vs 2.9.0)
   - ffmpeg API breakage (6.x vs 8.x)
   - PyAV incompatibilities across architectures

### Process Insights

1. **MVP Flexibility**: Adjusted from 3-way to 2-way comparison when models failed
2. **Journey Over Perfection**: Honest about blockers, focused on learnings
3. **Measurement Matters**: librosa quantifies the quality gap objectively

---

## Presentation Flow (Total: 12 min)

1. **Introduction** (2 min): Question, experiment scope, journey approach
2. **Baseline Demo** (1 min): Play 10s clip of Suno segment
3. **Local Models** (3 min): Bark success, Stable Audio/MusicGen failures
4. **Analysis Results** (3 min): Quantitative comparison (94% timbre, 4x noise)
5. **Lessons Learned** (2 min): Technical + process insights
6. **Q&A** (1 min): Anticipated questions

---

## Audio Files for Demo

**Location**: All files ready in project directories

**Suno Baselines** (`data/baseline/`):
- `suno_segment10_chorus.wav` (46.92s, 48kHz) - "Susurra Conmigo" chorus
- `suno_segment18_verse.wav` (19.60s, 48kHz) - "Caos y Suerte" verse

**Bark Outputs** (`results/local_models/`):
- `bark_segment10_chorus.wav` (14.36s, 24kHz) - Bark chorus attempt
- `bark_segment18_verse.wav` (13.91s, 24kHz) - Bark verse attempt

**Recommendation**: Play first 10 seconds of each pair for side-by-side comparison

---

## Key Metrics (Quick Reference)

| Metric | Segment 10 (Chorus) | Segment 18 (Verse) |
|--------|---------------------|-------------------|
| **Duration** | Suno: 46.92s / Bark: 14.36s | Suno: 19.60s / Bark: 13.91s |
| **Tempo** | Suno: 119.7 BPM / Bark: 127.8 BPM (+6.8%) | Suno: 119.7 BPM / Bark: 117.2 BPM (-2.1%) |
| **Timbre (MFCC)** | 0.934 similarity (93.4% match) | 0.940 similarity (94.0% match) |
| **Harmony (Chroma)** | 0.910 similarity (91.0% match) | 0.447 similarity (44.7% match) |
| **Noisiness (ZCR)** | +319% increase | +32% increase |
| **Loudness (RMS)** | +30% | +420% |

---

## Anticipated Q&A

**Q**: Why not just use Suno API?
**A**: Goal was local model comparison, not replicating Suno. Understanding limitations of open-source alternatives.

**Q**: Could Bark quality improve with fine-tuning?
**A**: Possibly, but fundamental architecture (TTS-based) limits music production quality. Would need music-specific training data + model modifications.

**Q**: Is this useful for production?
**A**: No. Quality gap too large. But useful for:
  - Research/experimentation
  - Understanding state of open-source AI music
  - Learning audio analysis techniques (librosa)

**Q**: What would make MusicGen work?
**A**: Either:
  1. Build custom PyAV wheel for ffmpeg 8.x
  2. Fork audiocraft to support newer PyAV versions
  3. Use older system ffmpeg (6.x) in isolated Docker environment with proper cross-compilation

Both require significant engineering effort beyond MVP scope.

**Q**: What's next?
**A**: For this research:
  - MusicGen Docker refinement (post-presentation)
  - Bark chunking for longer audio
  - Fine-tuning experiments

For practical music generation: Stick with Suno.ai until open-source catches up.

---

## Closing Message

> AI music generation is advancing rapidly, but commercial models (Suno) still lead open-source alternatives by a significant margin. Local generation is viable for experimentation, but production quality requires specialized models and infrastructure. The blockers we encountered (Stable Audio recursion, MusicGen dependencies) demonstrate that "open" doesn't always mean "deployment-ready."

> **The journey matters**: 4 days, 1 working model, 2 blocked models, comprehensive analysis. Honest learnings > polished demo.

---

**Prepared**: 2025-11-09
**Status**: Ready for Tuesday evening presentation
**Files Location**: `/Users/twin2/Desktop/projects/multiverse/research/code-first-protocol/`
