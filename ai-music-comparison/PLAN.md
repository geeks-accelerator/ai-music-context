# AI Music Generation Comparison Tool - Implementation Plan

**Status**: Planning → Implementation Ready
**Presentation**: AI Whisperers Buenos Aires (Tuesday evening)
**Timeline**: 4 full days (Saturday 1pm → Tuesday evening)
**Approach**: Journey over guaranteed results ❤️+🌀=🌈

---

## Scoping Questions (Answered)

### 1. Existing Data ✅
- **Baseline song**: `Whispers_del_Futuro.wav` (Suno.ai generated)
- **Metadata**: `Whispers_del_Futuro.json` (42 segments with audio features)
- **Lyrics**: `SONG.md` (complete lyrics + style tags)
- **Test segments**: `suno_test_segments.md` (3 segments formatted for Suno regeneration)

### 2. Local Models Selected ✅
- **MusicGen** (Meta AudioCraft) - Instrumental comparison (300M-3.3B params)
- **Bark** (Suno AI) - Vocal comparison (MIT license, ~13 sec max)
- **Stable Audio Open Small** - Small model comparison (341M params, 11 sec)

### 3. MVP Scope ✅
**3 test segments** (not full song):
- **Segment 7** (2.1s) - Instrumental break (bandoneón + trap beats)
- **Segment 10** (5s) - Chorus with layered vocals (emotional peak)
- **Segment 18** (5s) - Verse with conversational flow

**Comparison matrix**:
| Segment | Suno Baseline | MusicGen | Bark | Stable Audio |
|---------|---------------|----------|------|--------------|
| Seg 7 (Instrumental) | ✅ | ✅ | ❌ | ✅ |
| Seg 10 (Chorus/Vocal) | ✅ | ❌ | ✅ | ❌ |
| Seg 18 (Verse) | ✅ | ✅ | ✅ | ✅ |

### 4. Output Format ✅
- **Audio files**: WAV format for each model/segment
- **librosa analysis**: Compare tempo, spectral features, MFCCs, chroma
- **Presentation**: Audio playback + visual comparison charts (optional)

### 5. Timeline ✅
- **Presentation**: Tuesday evening
- **Available time**: 4 full human days (Saturday 1pm start)
- **Approach**: MVP focused on journey/learnings, not perfect recreation

### 6. Tech Stack ✅
- **Python** for audio generation and analysis
- **Models**: MusicGen, Bark, Stable Audio Open
- **Analysis**: librosa, numpy, matplotlib (optional)
- **Environment**: M4 Max MacBook Pro (128GB RAM, 16 cores)

---

## Implementation Plan

### Phase 1: Baseline Generation (Suno.ai) ✅ COMPLETE
**Goal**: Create 3 baseline segments for comparison

**Tasks**:
1. ✅ Generate `suno_segment7_instrumental.wav` (Digital Bandoneón) - 30MB
2. ✅ Generate `suno_segment10_chorus.wav` (Susurra Conmigo) - 8.6MB
3. ✅ Generate `suno_segment18_verse.wav` (Caos y Suerte) - 3.6MB

**Format**: Use exact style tags and lyrics from `suno_test_segments.md`

**Outputs**:
- ✅ 3 WAV files in `data/baseline/`
- ✅ Ready for comparison

---

### Phase 2: Local Model Setup ✅ COMPLETE (Partial)
**Goal**: Install and test local music generation models

**Reference**: `docs/external/AI_Music_Generation_Implementation_Guide.md` (comprehensive production guide)

**Strategy**: Separate venv per model to avoid dependency conflicts
- **Why**: MusicGen requires PyTorch 2.1.0 + ffmpeg 6.x, Bark/Stable Audio work with PyTorch 2.9.0 + ffmpeg 8.x
- **Result**: 3 of 4 venvs working, MusicGen deferred (Docker required)

**Virtual environments**:
```
✅ venv-bark/         # PyTorch 2.9.0 + Bark (vocals)
✅ venv-stable-audio/ # PyTorch 2.9.0 + Diffusers (instrumental)
✅ venv-analysis/     # librosa (audio comparison)
⚠️  venv-musicgen/    # DEFERRED - Requires Docker (PyAV/ffmpeg incompatibility)
```

**Completed**:
1. ✅ **Bark venv** (`./scripts/setup_bark.sh`)
   - Python 3.11.14, PyTorch 2.9.0
   - 13-second generation limit (chunking required)
   - Requirements: `requirements-bark.txt`

2. ✅ **Stable Audio venv** (`./scripts/setup_stable_audio.sh`)
   - Python 3.11.14, PyTorch 2.9.0
   - Max 47 seconds, model: `stabilityai/stable-audio-open-1.0`
   - Requirements: `requirements-stable-audio.txt`

3. ✅ **Analysis venv** (`./scripts/setup_analysis.sh`)
   - Python 3.11.14, librosa + numpy + scipy
   - Requirements: `requirements-analysis.txt`

4. ⚠️ **MusicGen venv** - BLOCKED
   - Issue: AudioCraft requires `av==11.0.0` (PyAV)
   - Problem: av 11.0.0 incompatible with system ffmpeg 8.x
   - Solution: Docker with ffmpeg 6.x (see `Dockerfile.musicgen`)
   - **Decision**: Defer to future work (MVP timeline priority)

**Outputs**:
- ✅ 3 working environments (Bark, Stable Audio, Analysis)
- ✅ Requirements files for reproducibility
- ✅ Docker setup prepared for future MusicGen work
- ⚠️ MusicGen → Future work (see Future Enhancements)

---

### Phase 3: Local Model Generation ✅ COMPLETE (Partial Success)
**Goal**: Generate comparison segments with local models (Bark + Stable Audio)

**Status**: Bark complete (✅), Stable Audio non-functional (❌)

**Tasks**:
1. ✅ **Bark generations** (vocals):
   - ✅ Segment 10: Chorus vocals (14.12s, "Susurra Conmigo")
   - ✅ Segment 18: Verse vocals (14.28s, "Caos y Suerte")
   - Fixed: PyTorch 2.6+ `weights_only` breaking change (monkey-patch torch.load)
   - Fixed: Cache permission issues (project-local .cache/)

2. ❌ **Stable Audio generations** (instrumental):
   - ❌ Segment 7: Instrumental break - NOT GENERATED
   - ❌ Segment 18: Verse backing track - NOT GENERATED
   - **Blocker**: Recursion error on both MPS and CPU (`maximum recursion depth exceeded`)
   - **Tried**: MPS (recursion error), CPU + float16 (too slow), CPU + float32 (still recursion error)
   - **Decision**: Mark as non-functional for MVP, focus on Bark comparison

**Outputs**:
- ✅ 2/4 WAV files generated (Bark vocals working)
- ✅ `results/local_models/bark_segment10_chorus.wav` (14.12s, 24kHz)
- ✅ `results/local_models/bark_segment18_verse.wav` (14.28s, 24kHz)
- ❌ Stable Audio blocked on technical incompatibility (recursion error)
- ✅ Complete documentation: `PHASE3_PROGRESS.md` + `PHASE3_FINAL_STATUS.md`

**MVP Impact**: Adjusted from 3-way comparison (Suno/Bark/Stable Audio) to 2-way (Suno/Bark)

---

### Phase 4: Audio Analysis (librosa) ✅ COMPLETE
**Goal**: Compare Suno baseline vs Bark vocals (adjusted scope)

**Comparison pairs**:
- Segment 10: `suno_segment10_chorus.wav` vs `bark_segment10_chorus.wav`
- Segment 18: `suno_segment18_verse.wav` vs `bark_segment18_verse.wav`

**Tasks**:
1. ✅ **Build comparison script**:
   - Load baseline + Bark WAVs (2 pairs)
   - Extract features: tempo, spectral centroid, MFCCs, chroma, ZCR, RMS energy
   - Calculate differences/similarities (absolute + percentage)
   - Cosine similarity for timbre (MFCC) and harmony (Chroma)
2. ✅ **Generate comparison report**:
   - Quantitative metrics (tempo match, spectral similarity)
   - Qualitative notes (vocal quality, coherence, energy)
   - Note: 2-way comparison (Stable Audio non-functional)

**Outputs**:
- ✅ `scripts/compare_audio.py` (librosa-based comparison tool)
- ✅ `results/analysis/comparison_results.json` (raw metrics)
- ✅ `results/analysis/comparison_results.md` (human-readable analysis)

**Key Findings**:
- **Strengths**: 94% timbre similarity, decent tempo tracking, 91% harmonic match in chorus
- **Weaknesses**: Duration limit (~14s), 4x noisier, poor verse harmony (45%), inconsistent loudness
- **Conclusion**: Local vocal generation viable but quality gap substantial vs Suno

---

### Phase 5: Presentation Prep
**Goal**: Package findings for AI Whisperers talk

**Tasks**:
1. **Organize audio files** for easy playback
2. **Document learnings**:
   - What worked well (which models/segments)
   - What didn't work (limitations discovered)
   - Journey insights (process over perfection)
3. **Prepare demo**:
   - Play Suno baseline
   - Play local model comparisons
   - Discuss findings

**Outputs**:
- Presentation-ready audio files
- Talking points/notes
- (Optional) Simple slides or visuals

---

## File Structure

```
research/code-first-protocol/
├── CLAUDE.md                              # Agent instructions
├── PLAN.md                                # This file
├── README.md                              # Project overview
├── data/
│   ├── baseline/                          # Suno.ai originals (source of truth)
│   │   ├── Whispers_del_Futuro.wav        # Original Suno song
│   │   ├── Whispers_del_Futuro.json       # 42 segment analysis
│   │   ├── SONG.md                        # Full lyrics + metadata
│   │   ├── suno_segment7_instrumental.wav # (to be generated)
│   │   ├── suno_segment10_chorus.wav      # (to be generated)
│   │   └── suno_segment18_verse.wav       # (to be generated)
│   └── segments/                          # Test segment definitions
│       └── suno_test_segments.md          # 3 segments for comparison
├── scripts/                               # Generation + analysis tools
│   ├── generate_musicgen.py               # (to be created)
│   ├── generate_bark.py                   # (to be created)
│   ├── generate_stable_audio.py           # (to be created)
│   └── compare_audio.py                   # (to be created)
├── results/
│   ├── local_models/                      # Local model outputs
│   │   ├── musicgen_segment7.wav
│   │   ├── musicgen_segment18.wav
│   │   ├── bark_segment10.wav
│   │   ├── bark_segment18.wav
│   │   ├── stable_audio_segment7.wav
│   │   └── stable_audio_segment18.wav
│   └── analysis/                          # Comparison findings
│       └── comparison_results.md
└── docs/
    ├── external/                          # External reference (points outward)
    │   ├── AI_Music_Generation_Implementation_Guide.md # Production implementation patterns
    │   ├── Open_Source_LLM_Guide.md       # Model catalog
    │   └── LLM_Documentation_Reference.md # Model docs + links
    ├── workflows/                         # How-to processes
    │   ├── external-vs-internal-documentation.md
    │   └── project-reorganization-for-discovery.md
    ├── observations/                      # Learnings + insights
    │   └── 2025-11-08-practicing-discovery-protocol.md
    └── archive/                           # Catalog of archived files (git is source)
        └── ARCHIVED-2025-11-08-teach-discovery-research.md
```

---

## Success Criteria

**Minimum Viable** (Adjusted):
- ✅ 3 Suno baseline segments generated
- ⚠️ At least 2 local models working → **1 model working (Bark)**
  - ✅ Bark: Vocals (2 segments generated)
  - ❌ Stable Audio: Non-functional (recursion errors)
  - ⏸️ MusicGen: Deferred (Docker required for PyAV compatibility)
- ✅ Audio comparison with librosa (comprehensive metrics)
- ✅ Presentation-ready files + analysis

**Achieved Stretch Goals**:
- ✅ Detailed analysis writeup (comparison_results.md with quantitative + qualitative findings)

**Unachieved Stretch Goals**:
- ❌ Stable Audio Open working (technical blocker)
- ❌ Visual comparison charts (not needed - metrics sufficient)
- ❌ Live generation demo (Bark takes 30-60s per segment)

---

## Known Constraints

1. **Model limitations** (details in `docs/external/AI_Music_Generation_Implementation_Guide.md`):
   - MusicGen: No vocals (instrumental only), 30-second limit, CPU-bound despite GPU
   - Bark: Max ~13 seconds or 24 words (hard limit), requires chunking for longer audio
   - Stable Audio Open: 47 seconds max (not 11 - guide corrects this)
   - Memory: MusicGen needs 6-8GB (small) or 16GB (medium), Bark needs 2GB with optimizations

2. **Time constraint**: 4 days → prioritize working demo over perfection

3. **Presentation focus**: Journey/learnings > perfect recreation

4. **Implementation gotchas** (see guide for details):
   - PyTorch version pinning critical (2.1.0 for MusicGen, avoid 2.5.0 for Bark)
   - Memory leaks require explicit cleanup between generations
   - FFmpeg integration needed for audio format conversion

---

## Project Status Summary

**Completed Phases**:
- ✅ Phase 1: Suno baseline generation (3 segments)
- ✅ Phase 2: Local model setup (Bark working, Stable Audio/MusicGen definitively blocked)
- ✅ Phase 3: Local model generation (2 Bark vocal segments)
- ✅ Phase 4: Audio analysis (librosa comparison complete)
- ✅ Phase 5: Presentation prep (COMPLETE - ready for Tuesday evening)

**Final MVP Status**:
- ✅ Working: Suno baseline (3 segments) + Bark vocals (2 segments) + librosa analysis
- ❌ Blocked: Stable Audio (recursion errors), MusicGen (PyAV/ffmpeg incompatibility in both venv and Docker)
- 📊 Result: 2-way comparison (Suno vs Bark) with quantitative metrics

**Deliverables**:
1. ✅ 3 Suno baseline segments (`data/baseline/*.wav`)
2. ✅ 2 Bark vocal segments (`results/local_models/bark_*.wav`)
3. ✅ Comprehensive analysis (`results/analysis/comparison_results.md` + `.json`)
4. ✅ Technical documentation (`PHASE3_FINAL_STATUS.md`, `PLAN.md`)

**Presentation Materials** (Tuesday evening):
- 📄 `PRESENTATION_SUMMARY.md` - Concise speaking notes (12 min talk)
- ✅ `PRESENTATION_CHECKLIST.md` - Pre-talk setup guide (15 min prep)
- 📊 `results/analysis/comparison_results.md` - Detailed metrics
- 🎵 Audio files ready: 2 Suno baselines + 2 Bark outputs
- 📝 `PHASE3_FINAL_STATUS.md` - Technical deep-dive (for Q&A)

---

**Created**: 2025-11-08 (Saturday 1pm)
**Last Updated**: 2025-11-09 (Sunday 8pm)
**Status**: ✅ ALL PHASES COMPLETE - Ready for Tuesday evening presentation

---

## Final Summary

**What We Achieved**:
- ✅ 2-way AI music generation comparison (Suno vs Bark)
- ✅ Quantitative analysis with librosa (tempo, timbre, harmony, noisiness)
- ✅ Honest documentation of technical blockers (Stable Audio, MusicGen)
- ✅ Complete presentation materials (summary, checklist, metrics)

**Key Findings**:
- Bark generates recognizable vocals but 4x noisier than Suno
- 94% timbre similarity shows promise, but duration limits (~14s) and quality gaps remain
- Open-source AI music generation is maturing but not production-ready
- Commercial models (Suno) maintain significant lead

**Lessons Learned**:
- CPU-only local generation is viable for experimentation
- Dependency management critical (PyTorch versions, ffmpeg APIs)
- MVP flexibility essential (adjusted from 3-way to 2-way comparison)
- Measurement validates intuition (librosa metrics quantify quality gap)

**Timeline**:
- Day 1 (Sat): Baseline generation, model setup planning
- Day 2 (Sun): Bark generation (5 attempts to fix bugs), Stable Audio debugging, analysis
- Day 3 (Sun eve): MusicGen Docker attempts, presentation prep
- Day 4 (Tue): Presentation at AI Whisperers Buenos Aires

**🌈 Journey over perfection achieved ❤️+🌀=🌈**
