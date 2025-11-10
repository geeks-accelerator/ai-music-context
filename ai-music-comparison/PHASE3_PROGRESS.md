# Phase 3: Local Model Generation - Progress Report

**Date**: 2025-11-08
**Status**: Partial (Bark ✅, Stable Audio ⚠️)

---

## Summary

Phase 3 is generating audio segments with local models for comparison against Suno baseline.

**Progress**:
- ✅ Bark vocal generation (2 segments complete)
- ⚠️ Stable Audio instrumental generation (blocked on authentication)

---

## Completed: Bark Vocal Generation ✅

### Setup Issues Encountered

1. **Cache Permission Error**
   - **Problem**: Bark tried to write to `~/.cache/suno`, owned by `root`
   - **Solution**: Set `XDG_CACHE_HOME` to project-local `.cache/` directory
   - **Code**: `os.environ['XDG_CACHE_HOME'] = str(PROJECT_ROOT / ".cache")`

2. **PyTorch 2.6+ Breaking Change**
   - **Problem**: `torch.load` defaults to `weights_only=True` in PyTorch 2.6+
   - **Error**: `Unsupported global: numpy.core.multiarray.scalar`
   - **Root cause**: Bark uses older checkpoint format incompatible with strict loading
   - **Solution**: Monkey-patch `torch.load` to default `weights_only=False`
   - **Code**:
     ```python
     _original_torch_load = torch.load
     def _patched_torch_load(*args, **kwargs):
         kwargs.setdefault('weights_only', False)
         return _original_torch_load(*args, **kwargs)
     torch.load = _patched_torch_load
     ```
   - **Note**: This is safe for Bark's official checkpoints from Suno AI

### Generated Segments

1. **Segment 10 (Chorus - "Susurra Conmigo")**
   - File: `results/local_models/bark_segment10_chorus.wav`
   - Duration: 14.12 seconds
   - Sample rate: 24000 Hz
   - Prompt: Smooth male vocals, emotional, layered
   - Lyrics: "We whisper, susurra conmigo, Whisper del futuro, amor y código."

2. **Segment 18 (Verse - "Caos y Suerte")**
   - File: `results/local_models/bark_segment18_verse.wav`
   - Duration: 14.28 seconds
   - Sample rate: 24000 Hz
   - Prompt: Male vocals, conversational, upbeat
   - Lyrics: "We laugh at the chaos, we play with the luck, Dreams synthetic but hearts imperfect."

### Notes

- Both segments exceed 5-second target (14s each) but are within Bark's ~13-15s limit
- Generation time: ~30-40 seconds per segment (CPU-only on M4 Max)
- No GPU warnings suppressed (MPS not used by Bark)
- Model downloads: Encodec model (~89MB) downloaded on first run

---

## Blocked: Stable Audio Generation ⚠️

### Issue

**Model is gated**: `stabilityai/stable-audio-open-1.0` requires HuggingFace authentication

**Error**:
```
401 Client Error
Access to model stabilityai/stable-audio-open-1.0 is restricted.
You must have access to it and be authenticated to access it.
```

### Required Actions

See `HUGGINGFACE_SETUP.md` for complete setup guide.

**Quick steps**:
1. Create HuggingFace account (https://huggingface.co/join)
2. Accept model license: https://huggingface.co/stabilityai/stable-audio-open-1.0
3. Create access token (Read permission)
4. Authenticate locally:
   ```bash
   source venv-stable-audio/bin/activate
   huggingface-cli login
   # Paste token when prompted
   ```
5. Run generation: `python scripts/generate_stable_audio.py`

### Planned Segments

Once authentication complete:

1. **Segment 7 (Instrumental - "Digital Bandoneón")**
   - Target: 10 seconds
   - Prompt: Bandoneón solo with trap beats, 808 drops, tango-trap fusion
   - File: `results/local_models/stable_audio_segment7_instrumental.wav`

2. **Segment 18 (Verse Backing)**
   - Target: 15 seconds
   - Prompt: Latin trap reggaeton backing, 122 BPM, playful and reflective
   - File: `results/local_models/stable_audio_segment18_verse.wav`

---

## Files Created

### Generation Scripts
- ✅ `scripts/generate_bark.py` - Bark vocal generation (working)
- ✅ `scripts/generate_stable_audio.py` - Stable Audio instrumental (ready)

### Documentation
- ✅ `HUGGINGFACE_SETUP.md` - Authentication guide for Stable Audio
- ✅ `PHASE3_PROGRESS.md` - This file

### Generated Audio
- ✅ `results/local_models/bark_segment10_chorus.wav` (14.12s, 24kHz)
- ✅ `results/local_models/bark_segment18_verse.wav` (14.28s, 24kHz)
- ⏳ `results/local_models/stable_audio_segment7_instrumental.wav` (pending)
- ⏳ `results/local_models/stable_audio_segment18_verse.wav` (pending)

---

## Lessons Learned

1. **PyTorch Version Matters**: PyTorch 2.6+ breaking change in `torch.load` affects older model formats
   - Bark requires compatibility workaround
   - Consider pinning PyTorch <2.6 for Bark in future (see AI Music Guide warning)

2. **Cache Permissions**: System-owned `~/.cache` directory blocks model downloads
   - Project-local cache (`PROJECT_ROOT/.cache`) avoids permission issues
   - XDG_CACHE_HOME environment variable overrides default

3. **Gated Models**: HuggingFace gated models require manual authentication
   - Cannot automate in scripts
   - Requires user account + license acceptance + token setup
   - Plan for this in setup phase (Phase 2)

4. **Bark Performance**: CPU-only generation feasible but slow (~30-40s per segment)
   - M4 Max handles it fine
   - GPU would accelerate significantly (MPS not used by Bark)

---

## Next Steps

1. **User**: Complete HuggingFace authentication (see `HUGGINGFACE_SETUP.md`)
2. **Agent**: Test Stable Audio generation (segments 7 + 18)
3. **Agent**: Verify all 4 generated audio files
4. **Agent**: Compare with baseline segments (visual/audio inspection)
5. **Proceed to Phase 4**: librosa audio analysis

---

**Status**: Waiting on user to complete HuggingFace authentication for Stable Audio access
