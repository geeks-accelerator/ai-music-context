# AI Music Generation Comparison - Presentation Outline

**Event**: AI Whisperers Buenos Aires
**Date**: Tuesday evening
**Duration**: TBD
**Approach**: Journey over perfection ❤️+🌀=🌈

---

## 1. Introduction (2 min)

**The Question**:
> Can local, open-source AI models generate music comparable to commercial services like Suno.ai?

**The Experiment**:
- Took 3 segments from Suno-generated song "Whispers del Futuro"
- Attempted to recreate vocals using local models
- Compared quality using librosa audio analysis

**The Journey**:
- 4 days of implementation (Saturday → Tuesday)
- Real-world constraints: timeline, hardware, compatibility issues
- Honest results: what worked, what didn't, why it matters

---

## 2. The Baseline: Suno.ai (2 min)

**What is Suno?**:
- Commercial AI music generation service
- Text prompts → full songs with vocals, instruments, production
- High quality, fast generation (~2-3 minutes per song)

**Our Test Segments**:
1. **Segment 7** (Instrumental): Digital bandoneón with trap beats (2.1s target)
2. **Segment 10** (Chorus): "Susurra Conmigo" - emotional vocal peak (5s target)
3. **Segment 18** (Verse): "Caos y Suerte" - conversational flow (5s target)

**Demo**: Play 10-second clips of each Suno segment

---

## 3. Local Model Exploration (5 min)

### Models Evaluated:

**1. Bark (Suno AI)** ✅
- Open-source TTS with singing capability
- MIT license, runs on CPU (no GPU required)
- Limit: ~13-15 seconds per generation
- **Result**: Successfully generated 2 vocal segments

**2. Stable Audio Open (Stability AI)** ❌
- Gated HuggingFace model for instrumental generation
- **Result**: Recursion errors on both MPS (Apple Metal) and CPU
- **Blocker**: Model compatibility issue, not configuration
- **Decision**: Marked as non-functional for MVP

**3. MusicGen (Meta AudioCraft)** ⏸️
- Instrumental generation (300M-3.3B params)
- **Result**: PyAV/ffmpeg incompatibility with system ffmpeg 8.x
- **Decision**: Deferred to Docker (out of scope for 4-day timeline)

### Technical Challenges:

**Bark Success Factors**:
- Fixed PyTorch 2.6+ breaking change (`weights_only=False` patch)
- Project-local cache directory (avoided permission issues)
- Translated Suno style tags to Bark prompt format

**Why Only 1 Model Worked**:
- Open-source AI music generation is still immature
- Dependency conflicts (PyTorch versions, ffmpeg, system libraries)
- Not all "open" models are deployment-ready

---

## 4. Audio Comparison Results (5 min)

### Methodology:

**librosa Audio Analysis**:
- Tempo (BPM)
- Timbre (MFCCs - vocal quality)
- Harmony (Chroma - pitch content)
- Brightness (Spectral centroid)
- Loudness (RMS energy)
- Noisiness (Zero-crossing rate)

### Key Findings:

#### What Bark Got Right ✅

**Timbre/Vocal Quality** (94% similarity):
- Segment 10: 0.934 MFCC match
- Segment 18: 0.940 MFCC match
- **Meaning**: Bark captures similar voice characteristics to Suno

**Tempo Tracking**:
- Segment 10: 119.7 BPM (Suno) vs 127.8 BPM (Bark) = +6.8%
- Segment 18: 119.7 BPM (Suno) vs 117.2 BPM (Bark) = -2.1%
- **Meaning**: Reasonable rhythm matching, especially in verse

**Harmonic Coherence (Chorus)** (91% similarity):
- Segment 10: 0.910 Chroma match
- **Meaning**: Bark follows melody well in emotional/chorus contexts

#### Where Bark Struggled ❌

**Duration Constraint**:
- Suno Segment 10: 46.92s → Bark: 14.36s (-69%)
- Suno Segment 18: 19.60s → Bark: 13.91s (-29%)
- **Meaning**: Bark hits hard limit, can't recreate full segments

**Noisiness/Artifacts** (4x worse):
- Segment 10: 0.0524 (Suno) vs 0.2195 (Bark) = +319% noise
- **Meaning**: Significant audio quality gap, audible artifacts

**Harmonic Accuracy (Verse)** (45% similarity):
- Segment 18: 0.447 Chroma match (LOW)
- **Meaning**: Struggles with melodic accuracy in conversational content

**Loudness Inconsistency**:
- Segment 10: +30% louder
- Segment 18: +420% louder (!)
- **Meaning**: Lacks nuanced dynamics, overcompensates in verse

**Demo**: Play side-by-side comparison (Suno vs Bark) for 1 segment

---

## 5. Lessons Learned (3 min)

### Technical Insights:

1. **Model Maturity Varies**:
   - Bark: Functional but limited (TTS-adapted, not music production)
   - Stable Audio: Gated but broken (recursion errors)
   - MusicGen: Requires Docker isolation (dependency hell)

2. **CPU-Only is Viable**:
   - Bark proves local generation works without GPU
   - 30-60 seconds per 14-second segment (acceptable for experimentation)

3. **Quality Gap is Real**:
   - 94% timbre similarity sounds impressive...
   - ...but 4x noisier + duration limits = unusable for production
   - Commercial models (Suno) have massive lead

### Process Insights:

1. **MVP Flexibility**:
   - Started: 3-way comparison (Suno/Bark/Stable Audio)
   - Adjusted: 2-way comparison (Suno/Bark only)
   - **Outcome**: Delivered meaningful results within timeline

2. **Journey Over Perfection**:
   - Honest about blockers (Stable Audio, MusicGen)
   - Focused on what worked (Bark + analysis)
   - Documented learnings (PHASE3_FINAL_STATUS.md)

3. **Measurement Matters**:
   - librosa quantitative analysis validates subjective assessment
   - Numbers make the quality gap undeniable (94% timbre but 4x noise)

---

## 6. What This Means (2 min)

### For AI Music Enthusiasts:

**Good News**:
- Local AI vocal generation is possible (Bark proves concept)
- Open-source models exist (MIT license, community-driven)
- Runs on consumer hardware (M4 Max, CPU-only, 128GB RAM)

**Reality Check**:
- Quality gap with commercial models is substantial
- "Open" doesn't mean "production-ready"
- Dependency management is critical (PyTorch versions, ffmpeg, etc.)

### For Developers:

**Lessons**:
1. Separate venvs per model (avoid dependency conflicts)
2. Expect compatibility issues (PyTorch breaking changes, system library mismatches)
3. Docker may be required (PyAV/ffmpeg, CUDA versions)
4. MVP scope flexibility is essential (adjust to reality)

**Resources**:
- Full implementation guide: `docs/external/AI_Music_Generation_Implementation_Guide.md`
- Technical deep-dive: `PHASE3_FINAL_STATUS.md`
- Code: `scripts/generate_bark.py`, `scripts/compare_audio.py`

### For the Future:

**Hypothesis Confirmed**:
- Local models CAN generate vocals from text prompts ✅

**Reality Validated**:
- Production-quality music generation requires specialized models (Suno), not adapted TTS (Bark) ✅

**Next Steps**:
- MusicGen Docker implementation (instrumental comparison)
- Stable Audio debugging (or wait for model updates)
- Fine-tuning experiments (adapt Bark to music domain?)

---

## 7. Q&A Preparation

### Anticipated Questions:

**Q**: Why not just use Suno API?
**A**: Goal was local model comparison, not replicating Suno. Understanding limitations of open-source alternatives.

**Q**: Could Bark quality improve with fine-tuning?
**A**: Possibly, but fundamental architecture (TTS-based) limits music production quality. Would need music-specific training data.

**Q**: Why did Stable Audio fail?
**A**: Recursion error appears to be model bug, not configuration. Tried MPS, CPU, float16, float32, reduced steps - all failed.

**Q**: Is this useful for production?
**A**: No. Bark quality gap too large. But useful for:
  - Research/experimentation
  - Understanding state of open-source AI music
  - Learning audio analysis techniques (librosa)

**Q**: What hardware did you use?
**A**: M4 Max MacBook Pro, 128GB RAM, 16 cores. Bark ran CPU-only (~30-60s per 14s segment).

**Q**: Can I try this myself?
**A**: Yes! Code in GitHub (research/code-first-protocol/). Setup scripts: `scripts/setup_bark.sh`, `scripts/setup_analysis.sh`.

---

## 8. Closing (1 min)

**The Takeaway**:
> AI music generation is advancing rapidly, but commercial models (Suno) still lead open-source alternatives by a significant margin. Local generation is viable for experimentation, but production quality requires specialized models and infrastructure.

**The Journey Matters**:
- 4 days: 1 working model, 2 blocked models, comprehensive analysis
- Honest learnings > polished demo
- Measurement validates intuition (94% timbre similarity, 4x noisier)

**Thank You**:
- AI Whisperers community for the opportunity
- Open-source maintainers (Bark, librosa, Suno AI)
- Questions welcome!

---

## Appendix: File Inventory for Demo

### Audio Files (for playback):

**Suno Baselines** (`data/baseline/`):
- `suno_segment10_chorus.wav` (46.92s, 48kHz)
- `suno_segment18_verse.wav` (19.60s, 48kHz)

**Bark Outputs** (`results/local_models/`):
- `bark_segment10_chorus.wav` (14.36s, 24kHz)
- `bark_segment18_verse.wav` (13.91s, 24kHz)

### Analysis Results (`results/analysis/`):
- `comparison_results.md` (human-readable findings)
- `comparison_results.json` (raw metrics)

### Technical Documentation:
- `PLAN.md` (project roadmap + status)
- `PHASE3_FINAL_STATUS.md` (technical deep-dive)
- `scripts/generate_bark.py` (generation code)
- `scripts/compare_audio.py` (analysis code)

---

**Presentation prepared**: 2025-11-09
**Status**: Ready for Tuesday evening demo
**Backup plan**: If audio playback unavailable, metrics + code walkthrough sufficient
