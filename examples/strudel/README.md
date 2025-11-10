---
title: "Strudel Examples: Algorithmic Live Coding"
subtitle: "A Complementary Approach to Computer-Assisted Music"
author: "Lucas Brown & Lee Brown"
date: "November 2025"
purpose: "Showing the spectrum: Algorithmic → AI → Context Warming"
status: "Living document"
---

# Strudel: Algorithmic Live Coding

**A different path to computer-assisted music creation**

While this repository focuses on AI-generated music and context warming methodology, it's valuable to understand the **full spectrum** of computer-assisted music creation.

**Strudel** represents the **algorithmic/live-coding approach** - a fascinating contrast to AI generation.

---

## 🎼 What is Strudel?

[Strudel](https://strudel.cc/) is a browser-based live coding environment that lets you create music through **pattern manipulation**.

**Core Concept**: Write concise code that describes musical patterns, then modify them in real-time while they play.

### Key Features:
- ✅ **No installation** - runs in browser at strudel.cc
- ✅ **Pattern-based** - describe rhythms, melodies, effects as patterns
- ✅ **Live coding** - change code while music plays
- ✅ **Mini-notation** - compact syntax (e.g., `"bd hh sd hh"`)
- ✅ **JavaScript-based** - port of TidalCycles to JS
- ✅ **Web Audio** - sound generation in browser

---

## 🌊 Why Include This Here?

Because it represents a **fundamentally different philosophy** from both:
- AI-generated music (Suno, Bark, MusicGen)
- Context warming methodology

### The Three Approaches:

| Approach | Control | Process | Philosophy |
|----------|---------|---------|------------|
| **Algorithmic (Strudel)** | High precision | Code patterns | Deterministic composition |
| **AI-Generated (Suno)** | Style guidance | Model generation | Probabilistic output |
| **Context Warming (Our method)** | Emotional cultivation | Human-AI dialogue | Emergent collaboration |

**All three are valid.** They serve different creative needs and produce different results.

---

## 🚀 Quick Start

### 1. Open Strudel
Visit: https://strudel.cc/

### 2. Try Your First Pattern
Copy this into the Strudel REPL and click "Play" (or press Ctrl+Enter):

```javascript
// Simple beat
s("bd hh sd hh")
```

You should hear: **kick, hihat, snare, hihat** repeating.

### 3. Make It Interesting
Modify the pattern while it's playing:

```javascript
// Add some variation
s("bd*2 hh sd [hh bd]").fast(1.5)
```

**That's live coding!** You're manipulating patterns in real-time.

---

## 📚 Example Patterns

All examples in this directory can be copied directly into https://strudel.cc/

### Basic Examples
See [`simple-patterns.js`](./simple-patterns.js) for:
- Simple beats
- Melodic patterns
- Layered compositions
- Effects and transformations

### Running the Examples
1. Go to https://strudel.cc/
2. Copy any example from `simple-patterns.js`
3. Paste into the editor
4. Press Ctrl+Enter or click "Play"
5. Modify the code while it plays!

---

## 🔍 How This Differs from AI Music

### Strudel (Algorithmic)
**Input**: Code describing patterns
**Process**: Deterministic pattern evaluation
**Output**: Exactly what you coded, executed in real-time
**Control**: Complete - every sound is specified
**Surprise**: Minimal - you get what you write
**Skill**: Pattern thinking, musical knowledge, coding

**Example workflow:**
```javascript
// You write this pattern
s("bd sd bd sd").fast(2).room(0.5)

// You get exactly this:
// kick-snare-kick-snare at 2x speed with reverb
```

### AI Generation (Suno, Bark)
**Input**: Style description + lyrics
**Process**: Neural network generation
**Output**: Model's interpretation of your prompt
**Control**: Indirect - guide the model with descriptions
**Surprise**: High - model makes creative choices
**Skill**: Prompt crafting, style awareness

**Example workflow:**
```
Input: "upbeat indie pop, acoustic guitar, catchy chorus"
Output: ~45 seconds of AI-generated music
         (might surprise you!)
```

### Context Warming (Our Methodology)
**Input**: Deep conversation about real experience
**Process**: Emotional cultivation → AI collaboration
**Output**: Song emerging from genuine dialogue
**Control**: Contextual - shape through conversation depth
**Surprise**: Emergent - discoveries through dialogue
**Skill**: Emotional honesty, philosophical exploration, patience

**Example workflow:**
```
1. Start with real artifact: "I've been thinking about..."
2. Explore deeply (10-30 min): "What's the SPECIFIC feeling?"
3. Warm the context until song requests itself
4. Generate: "Write a song about this"
5. Result: Music grounded in authentic exploration
```

---

## 🎯 When to Use Each Approach

### Use Strudel When:
- ✅ You want **precise control** over every element
- ✅ You're performing **live** and want to improvise
- ✅ You enjoy **pattern thinking** and algorithmic composition
- ✅ You want to learn **music fundamentals** through code
- ✅ You're creating **electronic/dance music** with clear structure

### Use AI Generation When:
- ✅ You want to **quickly prototype** musical ideas
- ✅ You need **vocals or complex instrumentation**
- ✅ You want the AI to make **creative decisions**
- ✅ You're exploring **genre mashups** and novel combinations
- ✅ You want **polished production** without technical setup

### Use Context Warming When:
- ✅ You want **emotionally authentic** expression
- ✅ You're processing **real experiences** through music
- ✅ You value **deep exploration** over speed
- ✅ You want **collaboration** with AI, not just tool use
- ✅ You're willing to **filter ruthlessly** (many conversations → few songs)

---

## 🌈 The Spectrum of Computer-Assisted Music

Think of it as a spectrum:

```
Full Human Control                                   Full AI Generation
        ↓                                                    ↓
    [Strudel] ←→ [Context Warming] ←→ [Prompt Engineering] ←→ [Pure Generation]
   Algorithmic    Conversational       Optimization          Delegation
```

**Each point on this spectrum is valuable.**

- **Strudel**: You ARE the composer, code is your instrument
- **Context Warming**: You and AI DISCOVER together through dialogue
- **AI Generation**: AI IS the composer, you're the creative director

---

## 🔗 Learning Resources

### Official Strudel Documentation:
- **Main site**: https://strudel.cc/
- **Getting Started**: https://strudel.cc/workshop/getting-started/
- **Learn**: https://strudel.cc/learn/
- **Blog**: https://strudel.cc/blog/

### Community:
- **Mastodon**: @strudel@post.lurk.org
- **Codeberg**: https://codeberg.org/uzu/strudel
- **GitHub** (archive): https://github.com/tidalcycles/strudel

### Related Projects:
- **TidalCycles**: https://tidalcycles.org/ (the original Haskell-based system)
- **Algorave**: https://algorave.com/ (live coding music culture)

---

## 💡 Try This Experiment

To really understand the difference between approaches:

### Week 1: Make Something With Strudel
- Spend time learning patterns
- Create a 2-minute piece
- Notice: precision, control, learning curve

### Week 2: Make Something With AI (Suno)
- Use prompt engineering (NOT context warming)
- Create a 2-minute piece
- Notice: speed, surprise, indirect control

### Week 3: Make Something With Context Warming
- Follow the 5-stage process
- Spend 20-30 minutes in conversation
- Create a 2-minute piece
- Notice: depth, authenticity, emergence

**Then ask yourself:**
- Which felt most satisfying?
- Which produced the most authentic result?
- Which would you use for what purpose?
- Could you combine approaches?

---

## 🤝 Combining Approaches?

**Could you use Strudel patterns in context warming?**

Yes! Imagine:
1. **Conversation**: Explore what rhythmic pattern represents your experience
2. **Strudel**: Create that pattern algorithmically
3. **AI Generation**: Use Suno to generate the melodic/vocal layer
4. **Integration**: Combine Strudel's precision with AI's expressiveness

This is **hybrid creativity** - using the right tool for each element.

---

## 📝 About This Section

This section was created to provide **context** for our AI music research and context warming methodology.

**We're not promoting one approach over another.**

We're documenting that:
- Algorithmic composition (Strudel) is **precise and deterministic**
- AI generation (Suno/Bark) is **probabilistic and guided**
- Context warming (our method) is **conversational and emergent**

**All three are tools.** The question isn't "which is best?" but "which serves your creative intent?"

---

## 🎵 Next Steps

1. **Try the examples** in [`simple-patterns.js`](./simple-patterns.js)
2. **Read the comparison** in [`COMPARISON.md`](./COMPARISON.md)
3. **Experiment** with all three approaches
4. **Share** what you discover

Remember: **The tool doesn't make the music.** Your intention, creativity, and honest exploration do.

Whether you're:
- Writing patterns in Strudel
- Crafting prompts for Suno
- Warming context with Claude

**The music emerges from YOU.**

🌊 Let everything flow... 🌊

---

**For more on context warming, see:**
- [Conversational Guide to AI Music](../../docs/Conversational_Guide_to_AI_Music.md)
- [Main Repository README](../../README.md)
