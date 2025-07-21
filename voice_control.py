import queue
import sounddevice as sd
import vosk
import json
import threading
import sys
import os

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

def asset_path(*path_parts):
    return os.path.join(base_path, *path_parts)


# Shared voice control flags
voice_state = {
    "left": False,
    "right": False,
    "up": False,
    "down": False,
    "fire": False
}
# Add this inside voice_control.py
menu_commands = {
    "start": False,
    "close": False,
    "level": None  # Will be set to 1, 2, 3, or 4
}

# Load model once
model = vosk.Model(asset_path("models", "vosk-model-small-en-us-0.15"))


q = queue.Queue()

def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def listen_for_commands():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=audio_callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        print("[Voice control started...]")

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print("Heard:", text)
                    update_flags(text)

def update_flags(command):
    global voice_state

    # Movement
    if "left" in command:
        voice_state["left"] = True
        voice_state["right"] = False
    elif "right" in command:
        voice_state["right"] = True
        voice_state["left"] = False
    elif "up" in command:
        voice_state["up"] = True
        voice_state["down"] = False
    elif "down" in command:
        voice_state["down"] = True
        voice_state["up"] = False
    elif "stop" in command:
        voice_state["left"] = voice_state["right"] = False
        voice_state["up"] = voice_state["down"] = False
    
    # Fire
    if "fire" in command:
        voice_state["fire"] = True
    if "cease fire" in command or "stop fire" in command:
        voice_state["fire"] = False
    if "start" in command:
        menu_commands["start"] = True
    if "quit" in command:
        menu_commands["close"] = True
    if "level one" in command:
        menu_commands["level"] = 1
    elif "level two" in command:
        menu_commands["level"] = 2
    elif "level three" in command:
        menu_commands["level"] = 3
    elif "level four" in command:
        menu_commands["level"] = 4