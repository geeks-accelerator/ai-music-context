// ============================================================
// Strudel Pattern Examples
// Copy any of these into https://strudel.cc/ and press Ctrl+Enter
// ============================================================

// ============================================================
// EXAMPLE 1: Your First Beat
// ============================================================
// The simplest pattern - just 4 sounds repeating
// bd = bass drum, hh = hihat, sd = snare drum

s("bd hh sd hh")

// Try modifying:
// - Change the order: s("bd sd hh hh")
// - Add more sounds: s("bd hh sd hh bd hh")
// - Use different samples: s("bd hh cp hh")  (cp = clap)


// ============================================================
// EXAMPLE 2: Adding Speed and Repetition
// ============================================================
// The * operator repeats elements
// The .fast() method speeds things up

s("bd*4 hh*8 sd*2 hh*4").fast(2)

// Try modifying:
// - Change repetition: s("bd*2 hh*4 sd hh*2")
// - Change speed: .fast(1.5) or .fast(0.5)
// - Mix patterns: s("[bd sd]*2 hh*4")


// ============================================================
// EXAMPLE 3: Rests and Silences
// ============================================================
// Use ~ for silence (rest)
// This creates space and rhythm

s("bd ~ sd ~ bd sd ~ ~")

// Try modifying:
// - More space: s("bd ~ ~ ~ sd ~ ~ ~")
// - Complex rhythm: s("bd [~ bd] sd [hh ~]")


// ============================================================
// EXAMPLE 4: Stacking Layers
// ============================================================
// stack() lets you play multiple patterns together
// Think of it like tracks in a DAW

stack(
  s("bd ~ bd ~"),           // kick on 1 and 3
  s("~ ~ sd ~"),            // snare on 3
  s("hh*8")                 // hihats throughout
)

// Try modifying:
// - Add a layer: s("~ cp ~ cp")
// - Change the hihat: s("hh*4 ~ hh*4 ~")
// - Add bass: note("c2 ~ c3 ~").s("sawtooth")


// ============================================================
// EXAMPLE 5: Melodic Patterns
// ============================================================
// Use note() or n() for melodies
// Numbers are MIDI notes (60 = middle C)

note("60 62 64 65").s("piano")

// Or use note names:
note("c4 d4 e4 g4").s("piano")

// Try modifying:
// - Different scale: note("c4 e4 g4 c5").s("sawtooth")
// - Add rhythm: note("c4*2 d4 e4 ~").s("piano")
// - Different sound: .s("glockenspiel")


// ============================================================
// EXAMPLE 6: Effects and Processing
// ============================================================
// Add effects with method chaining
// .room() = reverb, .delay() = echo, .lpf() = low-pass filter

s("bd hh sd hh")
  .room(0.5)        // reverb (0-1)
  .delay(0.25)      // echo amount
  .lpf(2000)        // filter cutoff frequency

// Try modifying:
// - More reverb: .room(0.8)
// - Different filter: .hpf(500)  (high-pass)
// - Distortion: .shape(0.5)
// - Crush: .crush(4)


// ============================================================
// EXAMPLE 7: Pattern Alternation
// ============================================================
// Use <> to alternate between patterns
// Great for variation

s("bd <sd cp> bd <sd [cp cp]>")

// Or alternate entire patterns:
s("<[bd sd] [bd*2 sd*2] [bd bd sd]>")

// Try modifying:
// - More variations: s("<bd cp lt> sd")
// - Speed changes: s("bd sd").fast("<1 2 1.5>")


// ============================================================
// EXAMPLE 8: Mini-Notation Power
// ============================================================
// Combine all the techniques for complex patterns

s("[bd sd bd sd] <hh*8 hh*16> ~ <cp lt>")

// Breakdown:
// [bd sd bd sd] = play these in sequence
// <hh*8 hh*16>  = alternate between 8 and 16 hihats
// ~             = rest
// <cp lt>       = alternate clap and low tom


// ============================================================
// EXAMPLE 9: A Complete Beat
// ============================================================
// Putting it all together into a full musical piece

stack(
  // Kick drum pattern
  s("bd ~ bd ~ bd ~ bd [~ bd]").room(0.2),

  // Snare on beats 2 and 4
  s("~ sd ~ sd").room(0.5),

  // Hi-hats with variation
  s("hh*8").gain("<0.6 0.8 0.7 0.9>"),

  // Percussion fills
  s("~ ~ ~ [cp cp]").delay(0.25)
)
.slow(0.8)  // adjust overall tempo

// Try modifying:
// - Change the feel: .fast(1.5) or .slow(1.2)
// - Add melody: note("c3 ~ g3 ~").s("sawtooth")
// - More effects: .shape(0.3) on any layer


// ============================================================
// EXAMPLE 10: Melodic Techno Loop
// ============================================================
// Bass + melody + rhythm

stack(
  // Deep bass line
  note("<c2 c2 g1 a1>").s("sawtooth")
    .lpf(800)
    .room(0.3),

  // Arpeggiated melody
  note("c4 e4 g4 e4 c5 e4 g4 e4")
    .s("triangle")
    .lpf(2000)
    .delay(0.5),

  // Rhythm section
  s("bd ~ ~ ~ bd ~ ~ [bd bd]"),
  s("~ sd ~ sd"),
  s("hh*16").gain(0.6)
)
.cpm(120)  // 120 cycles per minute

// Try modifying:
// - Different notes: "<c2 f2 g2 a1>"
// - Change arp: "c4 e4 [g4 a4] e4"
// - Add fills: s("~ ~ ~ [cp lt]")


// ============================================================
// EXAMPLE 11: Transformation Functions
// ============================================================
// Strudel has powerful transformation functions

s("bd sd")
  .every(4, x => x.fast(2))      // double speed every 4 cycles
  .sometimes(x => x.room(0.9))   // occasionally add reverb
  .off(0.125, x => x.speed(1.5)) // echo effect offset

// Try modifying:
// - .every(2, x => x.fast(4))    // more frequent changes
// - .rarely(x => x.shape(0.8))   // occasional distortion
// - .iter(4)                      // rotate pattern over 4 cycles


// ============================================================
// EXAMPLE 12: Euclidean Rhythms
// ============================================================
// Create interesting polyrhythms with euclid()

stack(
  s("bd").euclid(3, 8),    // 3 kicks distributed across 8 steps
  s("sd").euclid(5, 8),    // 5 snares distributed across 8 steps
  s("hh").euclid(7, 8)     // 7 hihats distributed across 8 steps
)

// This creates complex interlocking rhythms automatically!

// Try modifying:
// - Different distributions: euclid(5, 16)
// - Rotate: euclid(3, 8, 1)  (third param = rotation)
// - Stack more: s("cp").euclid(2, 5)


// ============================================================
// TIPS FOR LIVE CODING
// ============================================================

/*
1. START SIMPLE
   - Begin with s("bd sd")
   - Add complexity gradually while it plays

2. USE VARIABLES (commented out - uncomment to use)
   let kick = s("bd ~ bd ~")
   let snare = s("~ sd ~ sd")
   let hats = s("hh*8")
   stack(kick, snare, hats)

3. COMMENT OUT LAYERS
   - Use // to mute a layer
   - Great for building up/breaking down live

4. MODIFY WHILE PLAYING
   - Press Ctrl+Enter after each change
   - Music continues while you edit

5. EXPLORE THE SOUNDS
   Try different samples:
   - Drums: "bd", "sd", "hh", "cp", "lt", "ht"
   - Synths: "sawtooth", "square", "triangle", "sine"
   - Samples: "jazz", "sax", "amencutup", "birds"

   Use .bank() to switch sample sets:
   s("bd sd").bank("RolandTR909")
*/


// ============================================================
// CHALLENGE: CREATE YOUR OWN!
// ============================================================

/*
Try combining elements to create something unique:

1. Choose a tempo: .cpm(100)
2. Build a kick pattern: s("bd ~ ...")
3. Add a snare: s("~ sd ...")
4. Layer hihats: s("hh*8")
5. Add a bassline: note("c2 f2 ...").s("sawtooth")
6. Apply effects: .room(), .delay(), .lpf()
7. Add transformations: .every(), .sometimes()

Remember: Press Ctrl+Enter to hear changes immediately!
*/


// ============================================================
// RESOURCES
// ============================================================

/*
🌐 Official Site: https://strudel.cc/
📚 Documentation: https://strudel.cc/learn/
🎓 Tutorials: https://strudel.cc/workshop/
💬 Community: @strudel@post.lurk.org (Mastodon)

🔗 Related:
- TidalCycles (original): https://tidalcycles.org/
- Algorave (live coding culture): https://algorave.com/

✨ Sounds Library:
Explore all available sounds at: https://strudel.cc/sounds/
*/


// ============================================================
// HAVE FUN! 🌊
// ============================================================
// Remember: The best way to learn is to play
// Try things, break things, discover patterns
// There are no mistakes, only happy accidents
//
// Happy live coding! 🎵
