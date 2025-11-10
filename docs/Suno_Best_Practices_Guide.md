---
title: "Suno AI Best Practices Guide"
subtitle: "Technical Reference for AI Whisperers Buenos Aires"
author: "Lucas Brown & Lee Brown with AI collaboration"
date: "November 2025"
purpose: "Quick technical reference for Suno.com music generation"
status: "Living document"
---

# Suno AI Best Practices Guide
## Technical Reference for AI Whisperers Buenos Aires

A practical reference for the mechanics of creating music with Suno.com

---

**📚 Related Documents:**
- [Conversational Guide to AI Music](./Conversational_Guide_to_AI_Music.md) - Core methodology (read this first!)
- [Context Warming Novelty Research](./Context_Warming_Novelty_Research.md) - Why this approach is unique
- [Suno Master Guide](./Suno_Master_Guide.md) - Comprehensive technical guide with templates
- [AI Music Comparison Research](../ai-music-comparison/README.md) - Suno vs. Open-Source study

---

## Note: This Is the Technical Guide

This guide covers **Suno mechanics** - the tags, structures, and technical parameters.

**For the creative methodology** (context warming, emotional cultivation, the conversational approach), see:
→ **The Conversational Guide to AI Music**

This is the 5% technical work.  
That guide is the 95% creative work.

Use this as a quick reference when you're ready to generate.  
Use that guide to prepare what's worth generating.

---

## Understanding the Two Input Fields

### 1. Style of Music (up to 1000 characters, recommend under 500)
This is your **primary control** - Suno reads this FIRST to understand:
- Genre (trap, gospel, jazz-hop, synthwave)
- Mood (dark, uplifting, melancholic, cinematic)
- Instrumentation (808s, analog synths, orchestral strings)
- Vocal Style (male/female, whispery, layered, soulful)
- Structure hints (big chorus, slow build, ambient intro)

**Keep it concise** - while you can write up to 1000 characters, under 500 works best. Focus on the essential elements.

**Example:**
```
Uplifting gospel trap with 808s, female layered vocals, and a big cinematic chorus
```

### 2. Custom Lyrics
Where you put your actual lyrics with structure tags.
- Keep lines to **6-12 syllables** for best flow
- Use **[Square Brackets]** for section/verse labels, voice tags, instrument tags, mood markers, etc.
- Add **(Parentheses)** for ad-libs and backing vocals

**Square brackets can specify:**
- Section labels: [Verse 1], [Chorus], [Bridge]
- Voice tags: [Male Vocal], [Female Vocal], [Whispered]
- Instrument cues: [Guitar Solo], [Soft Piano Intro], [808s]
- Mood/energy: [Sad Verse], [Energy: High], [Emotional]
- Structure hints: [Build], [Drop], [Break]

---

## Using AI to Format Your Lyrics

**Pro Tip:** Let your AI conversation partner (Claude, ChatGPT) format the lyrics for Suno instead of doing it manually.

### After you have lyrics, ask:

**Step 1 - Format the lyrics:**
```
"Please format the lyrics for Suno.com LLM using [ ] for inline 
verse, style, voice tags"
```

**Step 2 - Generate style description:**
```
"Now can you provide a style description for Suno.com LLM in 500 
characters including the genre, bpm, voice, melody, rhythm..."
```

### Why this works:

- The AI understands Suno's syntax
- Ensures correct bracket usage: [ ] for tags vs ( ) for ad-libs
- Saves manual formatting time
- Less chance of errors that make tags audible when they shouldn't be

**Critical distinction:**
- **[Square brackets]** = Invisible tags (structure, mood, instructions)
- **(Parentheses)** = Audible ad-libs and backing vocals

Getting these wrong can result in the AI singing your tags out loud!

---

## Basic Song Structure Format

```
[Intro]
Optional instrumental opening or scene-setting

[Verse 1]
Your first verse lyrics here
Each line around 6-12 syllables
Build the story or theme

[Chorus]
The hook - most memorable part
Repeat key phrases
More melody and energy than verses

[Verse 2]
Add depth or new perspective
Continue the narrative
Maintain syllable rhythm

[Bridge]
Shift in mood or perspective
Often different melody
Provides variation

[Chorus]
Repeat your hook
Can add vocal layers or variations

[Outro]
Wrap up the song
Fade or final statement
```

---

## Essential Metatags

### Structure Tags
- **[Intro]** - Opening (can be instrumental)
- **[Verse]** or **[Verse 1], [Verse 2]** - Rhythmic, restrained sections
- **[Chorus]** - Melodic, energetic hook
- **[Pre-Chorus]** - Build anticipation before chorus
- **[Bridge]** - Variation/shift in mood
- **[Break]** - Instrumental section, silence from vocals
- **[Interlude]** - Instrumental within lyrics
- **[Outro]** - Ending section
- **[Hook]** - Repetitive phrase (repeat 2-4 times)

### Mood/Energy Tags (add to any section)
```
[Sad Verse]
[Happy Chorus]
[Emotional Bridge]
[Mood: Uplifting]
[Energy: High]
[Energy: Medium→High]
```

### Genre-Specific Tags (add to sections)
```
[Rapped Verse]
[Powerpop Chorus]
[Soft Piano Intro]
[Guitar Solo]
```

### Advanced Tags
```
[Instrument: 808s, Handclaps, Gospel Choir]
[Vocal Style: Whisper]
[Vocal Style: Power Praise]
[Vocal Effect: Reverb]
[Texture: Tape-Saturated]
[Tempo: Mid]
[Key: C minor]
```

---

## Vocal Style & Ad-libs

### In Style Box (200 char):
- "male vocalist, raspy"
- "female singer, soft airy vocals"
- "layered harmonies"
- "robotic vocoder effect"
- "soulful belting"

### In Lyrics (Parentheses):
Add backing vocals or ad-libs anywhere in your lyrics:
```
[Chorus]
We rise together (oh yeah!)
Hearts ignited (hearts ignited)
Moving forward (moving forward!)
Never divided (ooh-ooh)
```

### Voice Type Tags:
Can add to sections or style:
- [Male Vocal]
- [Female Vocal]
- [Girl] (younger voice)
- [Announcer] (speaking voice)

**Note:** Voice generation is somewhat random - these tags "nudge" but don't guarantee.

---

## Genre Examples

### For Trap/Hip-Hop:
```
Style: Dark trap with 808s, hi-hats, male vocals, aggressive flow

[Verse 1]
More words per line for faster rap delivery
Tighter syllable count keeps the energy up
```

### For Ballad/Slow:
```
Style: Emotional piano ballad, female vocals, slow build

[Verse 1]
Fewer words per line
Let each phrase breathe
Space for emotion
```

### For Gospel:
```
Style: Uplifting gospel with choir, organ, powerful female lead

[Chorus]
Praise with repetition (hallelujah!)
Call and response (yes Lord!)
Building intensity (oh oh oh!)
```

### For Electronic/EDM:
```
Style: Progressive house, 128 BPM, euphoric build, layered synths

[Build]
Instrumental rise
Energy climbing

[Drop]
Full synth assault (woah!)
Bass hits hard (yeah!)
```

---

## Pro Tips & Best Practices

**Note:** Suno is actively evolving. These tips are based on Suno v4.5/v5 capabilities as of late 2025. Some behaviors may change with future versions.

### ✅ DO:
1. **Be specific in style prompt** - "90s R&B love song with emotional depth" works better than just "R&B"
2. **Match syllable counts** - Verses need different phrasing than chorus or they blur together
3. **Use line breaks** - Helps AI understand rhythm and phrasing
4. **Keep it simple at first** - Start with 1-2 genre tags, don't overload
5. **Front-load important tags** - Put key tags in first 3-5 lines
6. **Limit instruments** - 2-3 specific instruments max to avoid dilution
7. **Experiment and iterate** - First generation might not be perfect

### ❌ DON'T:
1. **Don't use artist names** - Copyright restrictions (no "Elvis" or "Coldplay")
2. **Don't overload tags** - Too many conflicting instructions confuse the AI
3. **Don't mix too many genres** - 2 genres work (Gospel+Trap), 3-4 gets messy
4. **Don't use contradictory tags** - "very slow" + "high energy" will confuse
5. **Don't expect [Intro] to always work** - Sometimes "short instrumental intro" in style works better
6. **Don't assume tags are 100% reliable** - Think of them as nudges, not commands

### 💡 The Golden Rule:
**"Lyrics are stronger than metatags"**
- The lyric structure, syllable patterns, and your style prompt have MORE influence than tags
- Even when tags work, results can vary ("feels like a casino")
- Use tags to nudge, not to control every detail

---

## Special Techniques

### Sound Effects (use sparingly):
```
*gunshots*
*applause*
*phone ringing*
```

### Emphasis (ALL CAPS):
```
THIS IS IMPORTANT!
LOUDER DELIVERY!
```
Makes vocals more distinct or forceful.

### Instrumental Breaks:
```
[Instrumental]
[Break]
[Solo]
```

### Bilingual/Multilingual:
Just write lyrics in multiple languages - Suno handles it:
```
[Verse 1]
No es correr, es conexión
We run together, ritmo total
```

---

## Common Song Structures

### Pop Standard:
```
[Intro] → [Verse 1] → [Chorus] → [Verse 2] → [Chorus] → [Bridge] → [Chorus] → [Outro]
```

### Hip-Hop:
```
[Intro] → [Verse 1] → [Hook] → [Verse 2] → [Hook] → [Bridge] → [Hook] → [Outro]
```

### Electronic/EDM:
```
[Intro] → [Build] → [Drop] → [Break] → [Build] → [Drop] → [Outro]
```

### Ballad:
```
[Intro] → [Verse 1] → [Chorus] → [Verse 2] → [Chorus] → [Bridge] → [Final Chorus]
```

---

## Helpful Resources

### Official/Community:
- **Suno.wiki** - https://www.suno.wiki/ (comprehensive community wiki)
- **Suno AI Wiki** - https://sunoaiwiki.com/ (metatag lists and tips)

### Detailed Guides:
- **Jack Righteous** - https://jackrighteous.com (extensive Suno guides and meta tag reference)
- **How to Prompt Suno** - https://howtopromptsuno.com (practical tutorials)

### Quick References:
- **Suno Prompt Generator** - https://sunoprompt.com (helps generate prompts)
- **Medium Guide** - Complete list of styles and genres

### Key Articles:
- "Where to Put Your Suno Prompt" (Jack Righteous) - Clarifies the two input fields
- "Structuring 3,000-Character Custom Lyrics Prompts" - Advanced lyric structuring
- "Suno AI Meta Tags & Song Structure Command Guide" - Comprehensive tag reference

---

## Quick Start Template

Copy this template and customize:

```
STYLE OF MUSIC:
[Genre] with [instruments], [vocal type], [mood/energy], [special elements]

LYRICS:
[Intro]
[Optional opening lines or instrumental note]

[Verse 1]
First verse lyrics here
6-12 syllables per line
Build your theme

[Chorus]
Hook with repetition
Memorable melody
Key message (ad-libs!)

[Verse 2]
Add new perspective
Keep similar structure
Maintain energy

[Bridge]
Shift the mood
Different angle
Build tension

[Chorus]
Repeat the hook
Maybe add layers (yeah!)
Bring it home

[Outro]
Closing statement
Fade or final punch
```

---

## Final Thoughts

**What This Guide Covers:**
- Suno mechanics and technical parameters
- Tag structures and formatting
- Genre options and style descriptions
- Quick reference for generation

**What This Guide Doesn't Cover:**
- **How to know what's worth creating** → See: Conversational Guide to AI Music
- **Context warming methodology** → See: Conversational Guide to AI Music
- **The 5-stage creative process** → See: Conversational Guide to AI Music
- **Emotional cultivation and honest exploration** → See: Conversational Guide to AI Music

**The Relationship:**

This guide = **The mechanics** (5% of the work)  
Conversational Guide = **The methodology** (95% of the work)

You need both:
- Use the Conversational Guide to **cultivate context** and discover what wants to be expressed
- Use this guide to **execute technically** when you're ready to generate

**Remember:**
- Suno is a creative partner, not a precise machine
- Results will vary - experimentation is key
- The first generation is rarely perfect
- But if you've warmed the context well, it will be close to what matters

**For AI Whisperers:**
The tools are powerful, but the human - the intention, the cultural context, the meaning-making, **the conversation before creation** - that's irreplaceable. 

Learn these mechanics, yes.  
But focus your energy on context warming.

*"Most people use AI to go faster. We use it to slow down."*

---

**Two Guides for AI Whisperers Buenos Aires:**
1. **Suno AI Best Practices Guide** (this document) - Technical reference
2. **Conversational Guide to AI Music** - Creative methodology

Created by Geeks in the Woods (Twin brothers)  
November 2025
