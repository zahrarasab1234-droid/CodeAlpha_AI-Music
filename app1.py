

try:
    import streamlit as st  # type: ignore[reportMissingImports]
except Exception:
    # Fallback for editors or environments without streamlit installed.
    # Provide a lightweight dummy to avoid import-time and common runtime failures.
    class _DummySt:
        class DummyCtx:
            def __enter__(self):
                return self
            def __exit__(self, exc_type, exc_value, traceback):
                return False

        def set_page_config(self, *args, **kwargs):
            return None

        def __getattr__(self, name):
            def _noop(*a, **k):
                if name == "selectbox":
                    options = a[1] if len(a) > 1 else k.get("options", [])
                    index = k.get("index", 0)
                    if options:
                        return options[index if 0 <= index < len(options) else 0]
                    return None
                if name == "slider":
                    return k.get("value", a[0] if a else None)
                if name == "button":
                    return False
                if name == "columns":
                    count = a[0] if a else 1
                    if isinstance(count, (list, tuple)):
                        count = len(count)
                    return tuple(self.DummyCtx() for _ in range(count))
                if name == "spinner":
                    return self.DummyCtx()
                return None
            return _noop
    st = _DummySt()
import numpy as np
import io
import wave
import random
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="CodeAlpha 3D Neural Acoustics", page_icon="🎵", layout="wide")

# ── ULTIMATE 3D IMMERSIVE MATRIX STYLING SHEET ──
CSS = """
<style>
/* Pure Cyber Space Dark Foundation */
.stApp {
    background: radial-gradient(circle at 50% 30%, #070d1e 0%, #010204 100%) !important;
    overflow-x: hidden;
}

/* 🛸 Perspective 3D Neon Grid Floor Effect */
.stApp::after {
    content: "";
    position: fixed;
    bottom: -10%; left: -5%;
    width: 110vw; height: 50vh;
    background-image: 
        linear-gradient(rgba(6, 182, 214, 0.1) 2px, transparent 2px),
        linear-gradient(90deg, rgba(6, 182, 214, 0.1) 2px, transparent 2px);
    background-size: 50px 50px;
    transform: perspective(300px) rotateX(65deg);
    z-index: 0;
    pointer-events: none;
    mask-image: linear-gradient(to top, rgba(0,0,0,1), rgba(0,0,0,0));
}

/* Floating 3D Glowing Music Symbols in Space */
.stApp::before {
    content: "🎵  🎶  ♩  ♪  ♫  ♬  ♭  ♮  ♯  🎵  🎶  ♪  ♫  ♬  ♩  ♪  ♫  ♬";
    position: fixed; 
    top: -5%; left: -5%;
    width: 120vw; height: 120vh;
    font-size: 38px;
    line-height: 160px;
    word-spacing: 120px;
    font-family: Arial, sans-serif;
    z-index: 0; 
    pointer-events: none;
    animation: neon3DMusicGlow 6s ease-in-out infinite alternate, spaceScroll 40s linear infinite;
    transform: perspective(500px) rotateX(15deg) rotateY(-5deg);
}

@keyframes neon3DMusicGlow {
    0% { 
        color: #06b6d4; 
        text-shadow: 0 0 15px rgba(6,182,212,0.6), 200px 100px 25px rgba(217,70,239,0.3);
        opacity: 0.2;
    }
    50% { 
        color: #d946ef; 
        text-shadow: 0 0 30px rgba(217,70,239,0.8), -150px 300px 40px rgba(6,182,212,0.5);
        opacity: 0.45;
    }
    100% { 
        color: #8b5cf6; 
        text-shadow: 0 0 20px rgba(139,92,246,0.6), 300px -50px 30px rgba(217,70,239,0.4);
        opacity: 0.25;
    }
}

@keyframes spaceScroll {
    0% { transform: perspective(500px) rotateX(15deg) rotateY(-5deg) translateY(0px); }
    100% { transform: perspective(500px) rotateX(15deg) rotateY(-5deg) translateY(-480px); }
}

/* Main Studio Typography */
.main-title {
    color: #ffffff !important; 
    font-size: 45px; 
    font-weight: 900; 
    margin-top: 5px;
    margin-bottom: 2px;
    text-shadow: 0 0 35px rgba(6, 182, 212, 0.9);
}
.sub-title {
    color: #22d3ee !important; 
    font-size: 13px; 
    font-weight: 800; 
    letter-spacing: 4.5px; 
    text-transform: uppercase; 
    margin-bottom: 40px;
}

/* Hyper-Visible Crystal Text Layers */
h2, h3, p, span, label, div[data-testid="stWidgetLabel"] p {
    color: #ffffff !important;
    font-weight: 700 !important;
    text-shadow: 0px 2px 5px rgba(0,0,0,1) !important;
}

/* 🧱 3D GLASSMORPHIC CONTAINER CARDS FOR GRIDS */
div[data-testid="stVerticalBlock"] > div {
    z-index: 1;
}

.stSelectbox, div[data-testid="stSlider"] {
    background: rgba(10, 18, 36, 0.7);
    border: 1px solid rgba(6, 182, 212, 0.3);
    border-radius: 12px;
    padding: 18px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6), inset 0 1px 2px rgba(255,255,255,0.1);
    backdrop-filter: blur(8px);
    margin-bottom: 15px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.stSelectbox:hover, div[data-testid="stSlider"]:hover {
    transform: translateY(-4px) scale(1.01);
    box-shadow: 0 20px 40px rgba(6, 182, 212, 0.2);
    border-color: rgba(6, 182, 212, 0.6);
}

/* Custom Dropdown Input Override */
.stSelectbox div[data-baseweb="select"] {
    background-color: #050914 !important;
    border: 1px solid #06b6d4 !important;
}

/* ⚡️ 3D NEON ACTION BUTTON */
div.stButton > button {
    background: linear-gradient(135deg, #06b6d4 0%, #8b5cf6 100%) !important;
    color: #ffffff !important;
    font-weight: 800 !important;
    font-size: 16px !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 14px 28px !important;
    box-shadow: 0 6px 20px rgba(6, 182, 212, 0.4);
    transition: all 0.2s ease-in-out !important;
    width: 100%;
}
div.stButton > button:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 12px 30px rgba(217, 70, 239, 0.6) !important;
}

/* 💎 3D DYNAMIC OUTPUT DECK BOARD */
.wave-status-3d { 
    background: linear-gradient(145deg, rgba(9, 14, 28, 0.95), rgba(4, 7, 15, 0.95)); 
    border: 2px solid #d946ef; 
    border-radius: 14px; 
    padding: 22px; 
    margin-top: 15px; 
    box-shadow: 0 20px 45px rgba(217, 70, 239, 0.25), inset 0 0 15px rgba(217, 70, 239, 0.1);
    transform: perspective(600px) rotateX(2deg);
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# Application Master Header
st.markdown('<h1 class="main-title">🎵 AI Music Generation </h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">CodeAlpha Artificial Intelligence Engine </p>', unsafe_allow_html=True)

# ── 20 HIGHLY DIFFERENT AUDIO PATTERNS & WAVE MODIFIERS ──
NOTES_FREQ = {
    'C3': 130.81, 'D3': 146.83, 'E3': 164.81, 'F3': 174.61, 'G3': 196.00, 'A3': 220.00, 'B3': 246.94,
    'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23, 'G4': 392.00, 'A4': 440.00, 'B4': 493.88,
    'C5': 523.25, 'D5': 587.33, 'E5': 659.25, 'F5': 698.46, 'G5': 783.99, 'A5': 880.00, 'B5': 987.77, 'C6': 1046.50
}

GENRES = {
    "1. Classical (Arpeggiated Piano)": {"scale": ['C4', 'E4', 'G4', 'B4', 'C5'], "progression": [[0], [2], [4], [1]], "wave": "sine", "mod": "arpeggio"},
    "2. Deep Ambient (Drone Waves)": {"scale": ['F3', 'C4', 'F4', 'G4'], "progression": [[0, 1, 2, 3]], "wave": "sine", "mod": "drone"},
    "3. Cyberpunk (Staccato Bassline)": {"scale": ['A3', 'C4', 'D4', 'G4'], "progression": [[0, 0], [2, 1], [3, 0]], "wave": "sawtooth", "mod": "staccato"},
    "4. Lo-Fi (Detuned Nostalgia)": {"scale": ['C4', 'F4', 'A4', 'C5'], "progression": [[0, 2], [1, 3]], "wave": "triangle", "mod": "detune"},
    "5. Cinematic (Sub-Harmonic Drone)": {"scale": ['A3', 'E4', 'A4'], "progression": [[0, 1], [0, 2]], "wave": "sine", "mod": "subharmonic"},
    "6. Jazz (7th Chord Stacks)": {"scale": ['C4', 'E4', 'G4', 'B4', 'D5'], "progression": [[0, 1, 2, 3], [1, 2, 3, 4]], "wave": "sine", "mod": "polyphonic"},
    "7. EDM (Hyper-Saw Pluck)": {"scale": ['G3', 'D4', 'G4', 'B4'], "progression": [[0], [2], [1], [3]], "wave": "sawtooth", "mod": "pluck"},
    "8. Industrial Techno (Metallic Ring)": {"scale": ['A3', 'B3', 'C4'], "progression": [[0, 1], [1, 2]], "wave": "sawtooth", "mod": "metallic"},
    "9. House (Syncopated Organ)": {"scale": ['A3', 'D4', 'F4', 'A4'], "progression": [[0, 2], [1, 3]], "wave": "triangle", "mod": "syncopated"},
    "10. Glitch Pop (Chipped Frequency)": {"scale": ['C4', 'G4', 'A4', 'E5'], "progression": [[0, 3], [2, 1]], "wave": "sine", "mod": "glitch"},
    "11. Delta Blues (Slide Tremolo)": {"scale": ['E3', 'A3', 'B3', 'D4'], "progression": [[0, 1], [2, 0]], "wave": "triangle", "mod": "tremolo"},
    "12. Heavy Metal (Double-Octave Crunch)": {"scale": ['E3', 'B3', 'E4'], "progression": [[0, 1, 2]], "wave": "sawtooth", "mod": "octavestack"},
    "13. Trap (Hi-Hat Cluster Burst)": {"scale": ['G3', 'C4', 'D4'], "progression": [[0], [1], [2]], "wave": "triangle", "mod": "burst"},
    "14. Future Bass (Modulated Wobble)": {"scale": ['F3', 'C4', 'A4'], "progression": [[0, 1, 2]], "wave": "sine", "mod": "wobble"},
    "15. Reggae (Offbeat Skank Skank)": {"scale": ['G3', 'B3', 'D4', 'G4'], "progression": [[0, 2], [1, 3]], "wave": "triangle", "mod": "offbeat"},
    "16. Funk (Slap Octave Groove)": {"scale": ['A3', 'E4', 'A4'], "progression": [[0], [2], [1], [2]], "wave": "sawtooth", "mod": "slap"},
    "17. Flamenco (Rapid Rasgueado Triplet)": {"scale": ['E3', 'F3', 'A3', 'B3'], "progression": [[0, 1, 2], [1, 2, 3]], "wave": "sine", "mod": "triplet"},
    "18. Deep House (Chilled Chord Pad)": {"scale": ['A3', 'E4', 'G4', 'B4'], "progression": [[0, 1, 2, 3]], "wave": "sine", "mod": "pad"},
    "19. 8-Bit Retro (Square Chiptune Loop)": {"scale": ['C4', 'E4', 'G4', 'C5'], "progression": [[0], [1], [2], [3]], "wave": "sawtooth", "mod": "chiptune"},
    "20. Disco (Octave-Jumping Basswave)": {"scale": ['F3', 'F4', 'A3', 'A4'], "progression": [[0], [1], [2], [3]], "wave": "triangle", "mod": "octavejump"}
}

def generate_wave(wave_type, t, freq, mod_type):
    # Dynamic Modification Engine based on pattern mode selected
    if mod_type == "detune":
        freq = freq + np.sin(2 * np.pi * 3 * t) * 1.5  # Vibrato effect
    elif mod_type == "wobble":
        return np.sin(2 * np.pi * freq * t) * (0.5 + 0.5 * np.sin(2 * np.pi * 4 * t))
    elif mod_type == "metallic":
        return 0.7 * np.sin(2 * np.pi * freq * t) + 0.3 * np.sin(2 * np.pi * (freq * 1.414) * t)

    if wave_type == "sine": return np.sin(2 * np.pi * freq * t)
    elif wave_type == "sawtooth": return 2 * (t * freq - np.floor(0.5 + t * freq))
    elif wave_type == "triangle": return 2 * np.abs(2 * (t * freq - np.floor(0.5 + t * freq))) - 1
    return np.sin(2 * np.pi * freq * t)

def synthesize_audio(genre_name, duration, bpm, creativity):
    sample_rate = 22050
    genre_data = GENRES[genre_name]
    scale, wave_type, progression, mod_type = genre_data["scale"], genre_data["wave"], genre_data["progression"], genre_data["mod"]
    
    beat_duration = 60.0 / bpm
    if mod_type in ["staccato", "burst"]: beat_duration /= 2  # Accelerated sub-patterns
    
    total_beats = int(duration / beat_duration)
    audio_buffer = np.array([], dtype=np.float32)
    
    for beat in range(total_beats):
        chord_indices = progression[beat % len(progression)]
        if random.random() < creativity and mod_type != "drone": 
            chord_indices = [random.randint(0, len(scale)-1) for _ in range(2)]
            
        t = np.linspace(0, beat_duration, int(sample_rate * beat_duration), False)
        beat_wave = np.zeros_like(t)
        
        for idx in chord_indices:
            note = scale[idx % len(scale)]
            if note in NOTES_FREQ: 
                beat_wave += generate_wave(wave_type, t, NOTES_FREQ[note], mod_type)
                
        # Applying dynamic structural envelopes based on patterns
        envelope = np.ones_like(t)
        if mod_type in ["pluck", "staccato", "burst"]:
            envelope = np.exp(-4 * np.linspace(0, 1, len(t)))  # Sharp snappy decay
        elif mod_type == "offbeat":
            envelope[:int(len(t)*0.4)] = 0  # Delayed rhythmic syncopation
        else:
            attack, decay = int(0.15 * len(t)), int(0.25 * len(t))
            envelope[:attack] = np.linspace(0, 1, attack)
            envelope[-decay:] = np.linspace(1, 0, decay)
            
        audio_buffer = np.append(audio_buffer, beat_wave * envelope)
        
    if np.max(np.abs(audio_buffer)) > 0: audio_buffer = audio_buffer / np.max(np.abs(audio_buffer))
        
    audio_ints = (audio_buffer * 32767).astype(np.int16)
    byte_io = io.BytesIO()
    with wave.open(byte_io, 'wb') as wav_file:
        wav_file.setnchannels(1); wav_file.setsampwidth(2); wav_file.setframerate(sample_rate); wav_file.writeframes(audio_ints.tobytes())
    return byte_io.getvalue()

# ── HORIZONTAL DUAL COLUMNS GRID SYSTEM ──
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("🎛️ Acoustic Configuration Parameters")
    genre = st.selectbox("Select Target Neural Genre Pattern (20 Advanced Sub-Algorithms):", list(GENRES.keys()), index=0)
    duration = st.slider("Target Audio Duration (Seconds):", min_value=4, max_value=20, value=12, step=2)
    bpm = st.slider("Tempo Matrix (BPM - Beats Per Minute):", min_value=60, max_value=160, value=120, step=10)
    creativity = st.slider("Neural Mutation Factor (Pattern Randomness):", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    st.write("")
    trigger_generation = st.button("⚡ Generate AI Music Sequence")

with col2:
    st.subheader("🔊 Synthesized Neural Output Workspace")
    if trigger_generation:
        with st.spinner("Processing architectural structural layers..."):
            wav_bytes = synthesize_audio(genre, duration, bpm, creativity)
            st.success("Advanced unique acoustic pattern matrix compiled!")
            st.markdown(
                f'<div class="wave-status-3d">'
                f'<span style="color:#22d3ee; font-weight:bold; font-size:16px;">🎼 Waveform Properties Generated (3D Render):</span><br>'
                f'<span style="color:#ffffff; font-size:14px;">• Selected Channel Pattern: <b>{genre}</b><br>'
                f'• Mathematical Modulation Type: <b>{GENRES[genre]["mod"].upper()} Engine</b><br>'
                f'• Core Rhythm Engine: <b>{bpm} BPM</b><br>'
                f'• Total Track Vector Length: <b>{duration} Seconds</b></span>'
                f'</div>', unsafe_allow_html=True
            )
            st.write("")
            st.write("### 💎 Master Playback Deck:")
            st.audio(wav_bytes, format="audio/wav")
            st.write("")
            st.download_button(label="⬇ Download Synthesized Master Audio (.WAV)", data=wav_bytes, file_name=f"codealpha_diff_pattern_{int(datetime.now().timestamp())}.wav", mime="audio/wav")
    else:
        st.info("System Idle. Adjust acoustic controllers on the left grid and trigger the generation sequence pipeline.")