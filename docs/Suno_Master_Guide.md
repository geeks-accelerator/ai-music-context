---
title: "Suno Master Guide (v5.2)"
subtitle: "Catchy Templates + Mashups + Positive Energy + Dual-Remix Method"
author: "Lee Brown with AI collaboration"
date: "November 2025"
purpose: "Comprehensive technical guide for Suno v4.5 music generation"
status: "Living document"
version: "5.2"
---

# Suno Master Guide (v5.2) – Catchy Templates + Mashups + Positive Energy + Dual-Remix Method

> Complete v4.5-ready playbook: structure-first templates, global genres, mashups, viral positivity protocol, and dual-remix methodology.
> Use the **Style of Music** line + **[Section]** tags. Duplicate **[Chorus]** blocks to repeat.

---

**📚 Related Documents:**
- [Conversational Guide to AI Music](./Conversational_Guide_to_AI_Music.md) - Core methodology (start here for philosophy!)
- [Context Warming Novelty Research](./Context_Warming_Novelty_Research.md) - Why context warming is unique
- [Suno Best Practices Guide](./Suno_Best_Practices_Guide.md) - Quick technical reference
- [AI Music Comparison Research](../ai-music-comparison/README.md) - Suno vs. Open-Source study

---

## ⚠️ IMPORTANT: Copyright & Remix Ethics

**Before remixing or creating any music, understand these principles:**

### What You Can Do
- ✅ Create completely original songs using these techniques
- ✅ Remix your own songs that you created
- ✅ Use these templates to compose new, original music
- ✅ Experiment with AI music generation for learning purposes

### What Requires Permission
- ⚠️ **Remixing someone else's song requires their explicit permission**
- ⚠️ Even AI-generated remixes involve the underlying composition rights
- ⚠️ Sharing remixes publicly requires proper licensing/permission
- ⚠️ Using copyrighted lyrics, melodies, or musical elements needs authorization

### For This Presentation/Workshop
- We'll demonstrate techniques using **original compositions only**
- Any remix examples shown are for **educational purposes**
- When practicing, start with your own original songs
- Respect artists' work - get permission before remixing others' music

### The Dual-Remix Agreement
When this guide suggests creating two remixes, **both versions must respect the original creator's rights**. The dual-remix method is a creative technique, not permission to use copyrighted material.

**Bottom Line:** AI tools make it easy to create music, but copyright laws still apply. Always create original content or get proper permissions!

---

## CRITICAL OUTPUT INSTRUCTION

**When remixing songs, ALWAYS provide BOTH versions:**

### Output Format:
```
## REMIX 1: [Respectful/Template Version]
Recommended Sliders – Weirdness: 35-45% • Style Influence: 70-80% • Audio Influence: N/A
[Visual Guide: Maintain original themes and complexity]
[Full lyrics...]

## REMIX 2: [Viral/Simplified Version]  
Recommended Sliders – Weirdness: 25-35% • Style Influence: 80-85% • Audio Influence: N/A
[Visual Guide: Universal, bright, TikTok-ready visuals]
[Full lyrics...]
```

**Never skip Remix 1!** It shows you understand the original before simplifying.

---

## NEW: Slider Recommendation Policy (v4.5)

**Always include a one-line slider suggestion before the lyrics.**  
Format:  
`Recommended Sliders – Weirdness: <##%> • Style Influence: <##%> • Audio Influence: <##% or N/A>`

### Visual Guide Addition:
After sliders, include:  
`[Visual Guide: <brief description of AI video generation themes>]`

Examples:
- `[Visual Guide: Fractal zooms, infinite mirrors, recursive patterns]`
- `[Visual Guide: Meditation to dance transformation, BPM-synced evolution]`
- `[Visual Guide: Paired dancers, split-screen synchronization, doubling effects]`

### Weirdness (creativity):
- Commercial/radio pop, country, jazz/classical: **20–40%**
- EDM/rock/rap mainstream: **30–55%**
- Afrobeats/Amapiano/Latin: **25–50%**
- Jersey Club/Indie/Alt: **35–60%**
- Hyperpop/experimental: **60–85%** (expect variance)

### Style Influence (faithfulness to the style line):
- Commercial/radio: **70–90%**
- Most pop/EDM/rap: **60–80%**
- Indie/alt/club: **50–70%**
- Experimental/hyperpop: **40–70%**

### Audio Influence (only when an audio upload is used):
- Re-imagining: **0–30%**
- Creative remix: **40–60%**
- Extension/continuation: **70–100%**

**Identity protection (rewrites/section remixes):** keep **Weirdness ≤ 50%** and **Style Influence ≤ 60%** to preserve the song's DNA.

**If the user explicitly asks for "lyrics only,"** omit the slider line and visual guide, but still choose settings internally.

---

## Section 0 – v4.5 Prompting & Tagging Notes (Reviewed)

### Core Idea
v4.5 responds best to a **concise Style of Music line** in the Style box and **square-bracket section tags** in **Custom Lyrics**. Other "tags" (moods, instruments, mix words, theory) are **soft influence**—good nudges, not guarantees.

### A) What's Unbounded vs Bounded

**Unbounded (creative freedom)**
- Natural language & metaphors: "voice like honey over gravel", "guitars crying in rain"
- Invented genres & mashups: "quantum jazz × arctic folk"
- Compound modifiers & scenic cues: "Tokyo night city-pop", "warehouse techno"
- Cultural/era references without artist names

**Bounded (practical limits)**
- **Style field**: plan for ~200 characters in the web app (some APIs allow more)
- **Lyrics field**: aim for ~3,000 characters in the UI (APIs may allow ~5,000)
- **Song length**: v4.5 generates up to ~8:00; use **Extend** to add more
- **Audio format**: exports are typically 48 kHz WAV; don't hardcode 44.1 kHz
- **Concurrency**: the web app usually allows a small number of parallel jobs (e.g., ~4)
- **Artist names**: avoid direct "sounds like [artist]". Describe features instead

> Weighting myth-busting: "First 20–30 words" is a useful front-load rule of thumb—but the **Style** line and **early section lines** carry the most practical weight. Keep high-value cues up front.

### B) Reliable Syntax vs Experimental

**Reliable (Use These)**
- Section tags in Custom Lyrics: `[Intro]` `[Verse]` `[Pre-Chorus]` `[Chorus]` `[Post-Chorus]` `[Bridge]` `[Drop]` `[Spoken]` `[Outro]`
- Production/arrangement tags: `[Orchestral Breakdown]` `[Full Orchestra Building]` `[Dramatic Fade]` `[Guitar Solo]` `[Dance Break]`
- Parentheses for ad-libs/backups: `(yeah)` `(hey)` `(ooh)`
- ALL CAPS **sparingly** for single-word shouts

**Experimental / Soft-Influence (Use Sparingly)**
- Curly braces for BGV/SFX: `{yeah yeah}` `{crowd noise}`
- Double-parentheses for pronunciation pacing: `((em-PHA-sis))`
- Negation/anti-tags: "no drums", "avoid reverb"
- Theory/engineering words, BPM numbers, time signatures, pitch notes: helpful hints, **not guaranteed**

**Important Update:** Asterisks for ambience (e.g., `*rain falling*`, `*crowd cheer*`) should be **converted to square brackets** for v4.5: `[Rain Falling]`, `[Crowd Cheer]`

### C) Personas, Stems, Uploads (Plan-Dependent)

- **Personas**: If available in your plan/workspace, they can stabilize a vocal timbre across songs
- **Stems**: Full per-stem export is not guaranteed in all plans/workflows
- **Uploads/Extend**: Use short seeds and **Extend** for genre switches or alternate endings

### D) Mini Workflow (v4.5)

1. **Title = Hook** (2–4 words)
2. **Style line**: 1 sentence, 2–3 ideas (genre/mashup + 1–2 production cues + tone)
3. **Sections**: structure with tags; 5–8-word lines; micro-hook in chorus
4. **Contrast**: quiet verse → lift pre → explosive chorus
5. **Chant**: 1–3-word chant in chorus/post-chorus
6. **Repeat**: paste the entire [Chorus] block where you want repeats
7. **Iterate**: tweak the Style line first; then adjust sections if needed

---

## Section 5 – AI Operator Appendix (Template Selector & Rewrite Rules)

### AI Operator Appendix – Template Selector & Rewrite Rules

**Role:** Compose or rewrite youth-friendly lyrics using the templates in this guide.  
**Output:** **BOTH REMIXES** with bracket tags, sliders, and visual guides. **Duplicate [Chorus] blocks** to repeat; never write "x2/x3".

#### CRITICAL: Two-Remix Output Rule
**ALWAYS provide both remixes when rewriting:**
1. **Remix 1:** Template-based version (respects complexity)
2. **Remix 2:** Viral simplified version (maximum catchiness)

**Include for each:**
- Slider recommendations
- Visual guide description
- Full lyrics with proper formatting

#### 1) Detect Task & Inputs
- **Task** = `rewrite` (preserve structure) or `new` (compose from brief)
- Extract: genres/mashups, mood, energy/tempo, languages, singer count, features (drop/dance break/rap/key change), audience (clean, young-adult)
- If the user supplies a **Style of Music** line, use it verbatim; otherwise synthesize one (≤ ~200 chars)

#### 2) Deterministic Template Routing

**Dance / Drop**
- EDM festival / 2 drops → **#23 EDM – Double-Drop Festival**
- Pre→Drop→Hook pop → **#2 Drop-Driven Pop/EDM**
- Amapiano (log-drum, airy) → **#27 Amapiano** / **#13**
- Afrobeats mid-tempo → **#26** / **#12**
- Latin + big drop → **M3** / **#25**

**Group / Bilingual**
- K-Pop group (rap + key up) → **#11 K-Pop**
- J-/C-/Mando-/Canto-/T-/V-/P-Pop → **#41/#42/#43/#44/#45/#46/#47**

**Pop & Band**
- Pure pop earworm → **#21 Pop – Hook Sandwich** / **#1 Hook-First Anthem**
- Pop-punk crowd chants → **#6**
- Rock (classic + alt break) → **#29**
- Country radio / duet → **#30** / **#8**

**Hip-Hop / Hybrids**
- Rap + sung hook → **#22** / **#4**
- PluggNB float → **#31**
- Jersey Club bounce → **#34** / **#14**

**Internet-Native / Niche**
- Hyperpop → **#35** / **#10**
- Shoegaze → **#36** (DnB twist: **M7**)
- Brazil/Drift Phonk → **#32/#33**
- Indie bedroom pop → **#39** / **#5**
- Jazz / Classical / Techno → **#37/#38/#40**

**Mashups (explicit)** → choose **M1–M8** accordingly

**Fallbacks**: Dance/euphoric → **#2**; anthemic pop → **#1**; story/ballad → **#3**

#### 3) Style Line Builder
`<Genre/mashup>; <energy/tempo>, <instrument focus>; <hook/chant vibe>; <tone: clean/youth-friendly>`

#### 4) Formatting Rules
- Keep section tags; **duplicate [Chorus]** for repeats
- Hook = **2–4 words** with open vowels; verses **5–8 words** per line
- Add a **chant** somewhere. Keep language **clean**
- Bilingual: romanize non-English lines; keep hook vowels open
- **Convert all asterisked notes to square brackets**: `*guitar solo*` → `[Guitar Solo]`

#### 5) Rewrite Mode
- Preserve structure and **rhyme positions**; keep similar syllable counts
- Retain the core meaning; refresh imagery with new, concrete visuals
- Map original sections to the closest template
- **Ensure all production notes use square brackets, not asterisks**

#### 6) Output Contract
**For Remix 1:**
- Title with complexity maintained
- Recommended Sliders (W: 35-45%, S: 70-80%)
- Visual Guide (original themes)
- Full lyrics with original depth

**For Remix 2:**
- Simplified 2-3 word title
- Recommended Sliders (W: 25-35%, S: 80-85%)
- Visual Guide (viral/universal themes)
- Simplified lyrics with repetition

---

## Section 7 – Creative Sliders Guide

### 7.1 Weirdness (Safe → Chaos)
- **0–20% Safe Zone:** predictable, radio-friendly, stays within genre
- **30–50% Balanced:** default-like creativity with structure intact
- **60–85% Experimental:** genre-bending, avant-garde, expect surprises

### 7.2 Style Influence (Loose → Strict)
- **40–60% Loose:** AI interprets style broadly, may drift
- **70–85% Balanced:** follows style description closely
- **85–100% Strict:** maximum adherence to style line

### 7.3 Audio Influence (Fresh → Clone)
- **0–30% Re-imagining:** uses audio as loose inspiration
- **40–60% Creative Remix:** balances original and new elements
- **70–100% Extension:** stays very close to the uploaded audio

---

## Section 8 – The Viral Remix Methodology

### 8.1 The Double-Remix Method
- **First Remix:** Apply template structure, maintain complexity
- **Second Remix:** MAXIMUM SIMPLIFICATION + viral hooks
- **Title Formula:** 2-3 words, often repeated (COPY THAT, MORE MORE, LEVEL UP UP)
- **ALWAYS OUTPUT BOTH VERSIONS FOR COMPARISON**

### 8.2 Positive Energy Principle
- **NEVER** default to existential crisis or negative spirals
- Transform challenges into GROWTH moments
- "Trust nothing" ❌ → "Double check" ✅
- Paranoia as PREPARATION, not fear
- Celebrate the learning, not the trauma

### 8.3 The TikTok-Ready Formula
- Hook = Title = Repeated phrase
- Post-Chorus with chantable elements
- BPM journeys for transformation videos
- Universal themes in specific contexts
- **Visual Guide should include TikTok-friendly transitions**

### 8.4 Weirdness Sweet Spots by Iteration
- **First Rewrite:** 35-45% Weirdness (creative but structured)
- **Final Simplification:** 25-35% Weirdness (accessible but unique)
- **Style Influence:** 70-85% (stay on-genre but fresh)

### 8.5 The Repetition Power Law
- Title appears 15+ times minimum
- Key phrase doubled/tripled (more more more)
- Post-chorus as hypnotic chant
- Endings echo the beginning

### 8.6 Transformation Narratives That Work
- Slow → Fast (LEVEL UP UP)
- Stuck → Free (FOUND IT)
- Confused → Clear (FLOW STATE)
- Separate → United (SAME SAME POWER)
- **Always END POSITIVE**

### 8.7 Community Energy Checklist
✅ Does it celebrate growth?  
✅ Does it build people up?  
✅ Is the paranoia protective, not destructive?  
✅ Would this make someone feel empowered?  
✅ Can everyone relate, not just specialists?

### 8.8 Visual Guide Principles
**For Remix 1 (Complex):**
- Maintain original artistic vision
- Complex visual metaphors allowed
- Can include abstract concepts

**For Remix 2 (Viral):**
- Simple, clear transformations
- Before/after visuals
- Bright, positive color progression
- Easy-to-follow narrative
- TikTok transition-friendly moments

---

## Section 9: The Dual-Remix Philosophy

> **Note:** "Dual-Remix" means creating two paired versions of the same song - this technique works whether you're working solo, with a collaborator, or just exploring different creative directions!

Every song deserves **TWO REMIXES** that are **BOTH OUTPUT:**
1. **The Respectful Remix** (maintains essence)
2. **The Viral Remix** (pure catchiness)

**Why?** Because the first shows you UNDERSTAND the original, the second shows you understand the AUDIENCE.

### The Dual-Remix Process

#### Stage 1: Initial Rewrite
- Respect the original's complexity
- Apply appropriate template structure
- Maintain thematic depth
- Weirdness: 35-45%
- Style Influence: 70-80%
- Visual Guide: Original themes, can be complex

#### Stage 2: Viral Simplification
- Extract the CORE emotion/message
- Simplify to 2-3 word hooks
- Make it universally relatable
- Add post-chorus chants
- Weirdness: 25-35%
- Style Influence: 80-85%
- Visual Guide: Universal, bright, transformation-focused

### Common Patterns in Successful Viral Simplification

**Title Evolution Examples:**
- The Cathedral's Code → CODE ECHO ECHO → COPY THAT
- Unified Stage → DANCE DANCE TWICE → MAKE IT DANCE
- Runtime Paranoia → CHECK IT TWICE → DOUBLE CHECK

**Visual Evolution Examples:**
- Complex code architecture → Digital dancers learning moves
- Infinite fractals → Simple zoom transitions
- Technical debugging → Before/after success moments

**Notice:** The final version is always:
- Shorter
- More action-oriented
- Repeatable/chantable
- Positive or empowering
- Visually simpler

### The Psychology of Viral Positivity

**People share songs that make them feel:**
- Empowered (LEVEL UP UP)
- Connected (SAME SAME POWER)
- Accomplished (FOUND IT)
- Energized (MORE MORE MORE)

**Visual elements people share:**
- Transformation moments
- Synchronization effects
- Before/after reveals
- Celebration scenes
- Relatable situations becoming extraordinary

**Avoid songs that make them feel:**
- Existentially uncertain
- Isolated or paranoid
- Helpless or stuck
- Negatively self-aware

### Remember: 
Simplification isn't dumbing down—it's finding the **UNIVERSAL TRUTH** in complex ideas!

---

## Section 10: Visual Guide Best Practices

### For AI Video Generation
When providing visual guides, consider:

**Technical Elements:**
- BPM sync points for transitions
- Color progression (dark→light for positive transformation)
- Key visual moments tied to chorus/drop
- Repetitive elements for hook reinforcement

**Common Successful Patterns:**
- Single person → Multiple (community/connection)
- Still → Motion (activation/energy)
- Monochrome → Color (discovery/joy)
- Chaos → Order (achievement/clarity)
- Small → Big (growth/expansion)

**TikTok-Specific Considerations:**
- Vertical format optimization
- 15-30 second highlight moments
- Clear visual hooks every 3-5 seconds
- Transition points for duets/reactions
- Memeable freeze frames

### Visual Guide Format
Always include after slider recommendations:
```
[Visual Guide: Start with X, transform to Y through Z. Key moments: A at chorus, B at bridge, C at final drop. Colors: progress from D to E. TikTok hook: F movement/transition.]
```

---

## Key Formatting Reminders for v4.5

✅ **Always use square brackets** for all production directions:
- `[Orchestral Breakdown]` not `*orchestral breakdown*`
- `[Full Orchestra Building]` not `*full orchestra building*`
- `[Dramatic Fade]` not `*dramatic fade*`
- `[Guitar Solo]` not `*guitar solo*` or `{guitar solo}`
- `[Rain Falling]` not `*rain falling*`
- `[Crowd Cheer]` not `*crowd cheer*`

✅ **Consistent section tags**: `[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Drop]`, `[Outro]`

✅ **Parentheses only for vocals**: `(yeah)`, `(ooh)`, `(hey)`

✅ **Duplicate full [Chorus] blocks** instead of using "x2" or "repeat"

✅ **ALWAYS OUTPUT BOTH REMIXES** when rewriting songs

---

## Appendix: The Positive Energy Transformation

When transforming any song, ask yourself:

1. **What's the growth moment here?**
2. **How can struggle become strength?**
3. **Where's the celebration in this challenge?**
4. **What universal feeling connects everyone?**
5. **How can we end on empowerment?**
6. **What visual journey supports this transformation?**

Every viral hit is an invitation to feel BETTER. Make your remixes deliver that feeling TWICE—once through understanding, once through pure catchiness!

**The Ultimate Goal:** Songs that make people want to hit replay, share with friends, and use in their own content—because the energy is so POSITIVE and INFECTIOUS, and the visuals are so SHAREABLE!

---

## Final Output Checklist

Before submitting any rewrite:
- [ ] Did I provide BOTH remixes?
- [ ] Does each have slider recommendations?
- [ ] Does each have a visual guide?
- [ ] Is Remix 1 respectful of the original?
- [ ] Is Remix 2 simplified and viral-ready?
- [ ] Are both titles clear and memorable?
- [ ] Do the visual guides progress from simple to extraordinary?
- [ ] Is the energy positive and empowering?
- [ ] Have I respected copyright and obtained necessary permissions?

---

## Quick Start Guide for Beginners

**New to Suno? Start here:**

1. **Your First Song (5 minutes)**
   - Pick a mood: happy, energetic, chill, powerful
   - Choose a genre you like: pop, EDM, rock, indie
   - Write 3-4 simple lines about something you care about
   - Click generate!

2. **Making It Better (10 minutes)**
   - Add a **Style of Music** line: "Upbeat pop with acoustic guitar, catchy hook"
   - Use section tags: `[Verse]` `[Chorus]` `[Verse]` `[Chorus]`
   - Keep lines short: 5-8 words max
   - Repeat your chorus by pasting it again

3. **Going Viral (Advanced)**
   - Use this guide's dual-remix method
   - Follow the slider recommendations
   - Add visual guides for social media
   - Focus on positive, empowering messages

**Remember:** Start simple, experiment often, and always create original content or get permission before remixing others' work!

---

*End of Guide v5.2 - Now with Copyright Guidance, Clearer Terminology, and Quick Start for Beginners!*

**Updates in v5.2:**
- Added comprehensive copyright and ethics section
- Replaced "Twin" terminology with "Dual-Remix" for clarity
- Added Quick Start Guide for complete beginners
- Enhanced presentation-ready formatting
- Clarified that dual-remix method works for all creators, not just twins
