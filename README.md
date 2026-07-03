# AI Music Generation & Synthesis Lab

Welcome to the **AI Music Generation & Synthesis Lab**! This is a fully interactive, web-based 3D cyberpunk studio that dynamically synthesizes custom audio tracks straight from mathematical waveforms—built purely with **Python, NumPy, and Streamlit**. 

I engineered this project as part of my Artificial Intelligence Internship at **CodeAlpha** (Task 3) to explore how digital signal processing and mathematics can create generative art.

---

## What Makes This Project Cool

* **Acoustic Matrix Controllers:** This is your control deck. You can fine-tune how the audio behaves before hitting generate.
  * **20 Unique Sub-Algorithm Channels:** Move away from basic loops! You can switch between 20 custom genre behaviors, from soothing *Classical Piano Serenades* and moody *Cyberpunk Synthwave* to chaotic *Glitch Pop* and raw *Industrial Techno*.
  * **BPM Rhythm Engine:** Bump up the speed or slow things down with a fluid tempo slider ranging from 60 to 160 BPM.
  * **Target Duration Control:** Generate exactly what you need, customizable from a quick 4-second loop up to a 20-second track segment.
  * **Neural Mutation Factor:** Want things unpredictable? Cranking this up introduces algorithmic randomness, creating unique variations every single time.
* **Synthesized Neural Output Workspace:** Once you click generate, this workspace compiles your track in real-time, displays the wave properties, lets you listen to it instantly with a native media player, and gives you a high-quality `.WAV` download button.
* **Immersive 3D Cyberpunk Visuals:** No basic layouts here! I customized the interface with dark glassmorphic card elements, glowing neon animations, and smooth floating music symbols to give it an authentic studio vibe.

---

## 🛠️ Tech Stack Used

* **Frontend & Interactive UI:** Streamlit (injected with custom CSS layouts for that slick neon look).
* **Audio Core Synthesis:** NumPy (used to crunch vector mathematics and build pure wave arrays).
* **Audio Output & Writing:** Native Python `wave` & `io.BytesIO` libraries to compress raw math arrays into listenable digital audio files.

---

## How It Works Under the Hood (Simply Put)

Instead of relying on pre-recorded audio samples, this engine creates music from absolute scratch using mathematics.

1. **Wave Generation:** When you select a track pattern, NumPy computes array vectors for raw signals like **Sine**, **Sawtooth**, or **Triangle** shapes based on musical note frequencies:
   * *Sine Wave:* $\sin(2\pi \cdot \text{Freq} \cdot t)$
   * *Sawtooth Wave:* $2 \cdot (t \cdot \text{Freq} - \lfloor 0.5 + t \cdot \text{Freq} \rfloor)$
2. **Scale & Chord Progressions:** The code reads complex scales and layers multiple note frequencies together to form chords.
3. **Envelope Shaping:** To prevent the audio from sounding like static noise, I implemented a smooth **Attack & Decay Envelope**. This means notes gracefully fade in and out like real instruments, creating crisp plucks, deep ambient pads, or heavy bass rhythms.

---

## Running It Locally

Want to try it out on your machine? It takes less than two minutes to set up:

### 1. Clone the Repo
```bash
git clone [https://github.com/zahrarasab1234-droid/CodeAlpha_AI-Music.git](https://github.com/zahrarasab1234-droid/CodeAlpha_AI-Music.git)
cd CodeAlpha_AI-Music
