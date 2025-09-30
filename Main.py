import kivy
kivy.require("2.1.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import sounddevice as sd
import numpy as np
import threading

# === Frequency Map (same as encoder) ===
FREQ_MAP = {
    '0': 1000,
    '1': 1200,
    '2': 1400,
    '3': 1600,
    '4': 1800,
    '5': 2000,
    '6': 2200,
    '7': 2400,
    '8': 2600,
    '9': 2800,
    'a': 3000,
    'b': 3200,
    'c': 3400,
    'd': 3600,
    'e': 3800,
    'f': 4000,
}

INV_FREQ_MAP = {v: k for k, v in FREQ_MAP.items()}

SAMPLE_RATE = 44100
DURATION = 0.25  # seconds per tone
TOLERANCE = 30   # Hz tolerance for detection


def closest_freq(freq):
    """Return closest valid frequency from map"""
    return min(FREQ_MAP.values(), key=lambda f: abs(f - freq))


def decode_audio(audio):
    """Decode recorded audio into hex string, then back to text"""
    step = int(DURATION * SAMPLE_RATE)
    chars = []
    for i in range(0, len(audio), step):
        chunk = audio[i:i+step]
        if len(chunk) < step:
            continue
        fft = np.fft.rfft(chunk)
        freqs = np.fft.rfftfreq(len(chunk), 1 / SAMPLE_RATE)
        peak = freqs[np.argmax(np.abs(fft))]
        if peak < 800:  # ignore noise
            continue
        freq = closest_freq(peak)
        chars.append(INV_FREQ_MAP.get(freq, ""))
    try:
        hex_string = "".join(chars)
        text = bytes.fromhex(hex_string).decode()
        return text
    except Exception:
        return None


class VQRApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.label = Label(text="🎙️ Press 'Listen' to decode VQR", font_size=20)
        self.layout.add_widget(self.label)

        self.listen_btn = Button(text="Listen", size_hint=(1, 0.2))
        self.listen_btn.bind(on_press=self.start_recording)
        self.layout.add_widget(self.listen_btn)

        return self.layout

    def start_recording(self, instance):
        self.label.text = "🎧 Listening..."
        threading.Thread(target=self.record_and_decode).start()

    def record_and_decode(self):
        try:
            audio = sd.rec(int(SAMPLE_RATE * 5), samplerate=SAMPLE_RATE, channels=1, dtype="float64")
            sd.wait()
            audio = audio.flatten()
            result = decode_audio(audio)
            if result:
                self.update_label(f"✅ Decoded URL:\n{result}")
            else:
                self.update_label("❌ Could not decode (CRC error)")
        except Exception as e:
            self.update_label(f"Error: {e}")

    def update_label(self, text):
        Clock.schedule_once(lambda dt: setattr(self.label, "text", text))


if __name__ == "__main__":
    VQRApp().run()
