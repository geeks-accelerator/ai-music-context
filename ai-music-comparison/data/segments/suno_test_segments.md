# Suno.ai Test Segments - Whispers del Futuro Comparison

Generated for AI music comparison experiment (Suno vs local open-source models)

---

## Segment 7 - Instrumental Break

**Title**: Digital Bandoneón

**Style Tags**:
```
[Latin trap / reggaetón / electronic milonga fusion]
[Tempo: mid-slow urban flow (120 BPM)]
[Mood: mystical + intense + rhythmic]
[Instrumental only - no vocals]
[Bandoneón solo with trap beats and 808 drops]
```

**Lyrics**:
```
[Intro - instrumental]
[Bandoneón solo with 808 drops]
[Trap beat with tango undertones]
[Build intensity]
[Drop]
```

**Duration Target**: ~10-15 seconds
**Audio Features**: High energy (0.85), percussive, trap-tango fusion

---

## Segment 10 - Chorus (Vocal + Instrumental)

**Title**: Susurra Conmigo

**Style Tags**:
```
[Latin trap / reggaetón / electronic milonga fusion]
[Tempo: mid-slow urban flow (120 BPM)]
[Mood: mystical + empowered + emotional]
[Voice: smooth male lead + female harmonies + layered vocals]
[Emotional intensity - peak chorus energy]
```

**Lyrics**:
```
[Chorus - layered vocals + female harmonies]
We whisper — (susurra conmigo)
Whisper del futuro, amor y código
We whisper — (susurra conmigo)
Entre el alma y la data, we make it musical

[Echo tail with vocal reverb: susurra… susurra…]
```

**Duration Target**: ~15-20 seconds
**Audio Features**: Highest intensity (1.40), layered vocals, emotional peak

---

## Segment 18 - Verse (Vocal + Instrumental)

**Title**: Caos y Suerte

**Style Tags**:
```
[Latin trap / reggaetón / electronic milonga fusion]
[Tempo: mid-slow urban flow (122 BPM)]
[Mood: playful + empowered + reflective]
[Voice: smooth male lead with natural tone variation]
[Upbeat verse with clear rhythm]
```

**Lyrics**:
```
[Verse - male lead]
We laugh at the chaos, we play con la suerte,
Dreams synthetic but hearts still imperfect.
Mientras el mundo corre, nosotros escuchamos,
La máquina escribe, pero humanos cantamos.

[Background vocals: susurra, susurra…]
```

**Duration Target**: ~15-20 seconds
**Audio Features**: Moderate intensity (1.03), upbeat, conversational flow

---

## Generation Instructions for Suno.ai

1. **Create each as a separate song** on Suno.ai
2. **Use Custom Mode** to input exact style tags
3. **Generate short clips** (aim for 15-20 seconds each)
4. **Download as WAV** for librosa comparison
5. **Save with clear naming**:
   - `suno_segment7_instrumental.wav`
   - `suno_segment10_chorus.wav`
   - `suno_segment18_verse.wav`

---

## Comparison Matrix

| Segment | Type | Suno Test | MusicGen Test | Bark Test | Stable Audio Test |
|---------|------|-----------|---------------|-----------|-------------------|
| **Seg 7** (Instrumental) | Instrumental break | ✅ | ✅ | ❌ | ✅ |
| **Seg 10** (Chorus) | Vocal + harmony | ✅ | ❌ | ✅ | ❌ |
| **Seg 18** (Verse) | Vocal + backing | ✅ | ✅ | ✅ | ✅ |

---

## Notes for Local Model Generation

### MusicGen (Instrumental comparison)
- Use segments 7 and 18
- Input: Text description of style/mood
- Compare: Tempo accuracy, melodic coherence, energy level

### Bark (Vocal comparison)
- Use segments 10 and 18
- Input: Exact lyrics text
- Compare: Vocal quality, emotional expression, pronunciation
- Note: Bark limited to ~13 seconds, may need to truncate

### Stable Audio Open (Small model comparison)
- Use segments 7 and 18
- Input: Text prompt describing audio characteristics
- Compare: Audio quality despite small size (341M params)
- Note: Limited to 11 seconds

---

**Created**: 2025-11-08
**For**: AI Whisperers Buenos Aires presentation
**Experiment**: Suno.ai vs local open-source music generation models
