

# 🌍 Voice Controlled space shooter

**Galaxy Fighter** is a 2D space shooter game made with **Python, Pygame, Vosk, and Sounddevice**.  
The game lets you control your spaceship with **your voice** — move left, move right, shoot, activate power-ups — alongside traditional keyboard controls.

---

## 🚀 Features

- **Classic 2D space shooter gameplay**
- **Voice control:** Say "left," "right," "up," "down," "fire," "start," "level one," etc.
- **Power-ups:** health, shield, rapid-fire
- **Boss fights:** Levels 2-4 feature a powerful boss at the last wave
- **Levels and waves:** The game progressively gets more challenging with each wave
- **Customizable:** Easily add more enemies, power-ups, or voice commands

---

## 🔹 Tech Stack

- **Python 3.7+**
- **Pygame:** rendering, game loop, collision, audio
- **Vosk:** speech-to-text for voice control
- **Sounddevice:** accessing raw audio from your microphone
- **JSON:** parsing voice recognizer output

---

## ⚙ Installation

1️⃣ **Clone this repository:**

```bash
git clone https://github.com/siddhantsaxena45/galactic-fighter.git
cd galactic-fighter
````

2️⃣ **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
source venv/bin/activate      # On Linux/Mac
```

3️⃣ **Install required packages:**

```bash
pip install -r requirements.txt
```

4️⃣ **Download Vosk Model (English Small or Large) from [Vosk models](https://alphacephei.com/vosk/models)**
Extract it into `models/vosk-model-small-en-us-0.15/`.

---

## 🕹 How to Play

* **Start game:** Say "start" or press the `Enter` key.
* **Move:** Say "left," "right," "up," or "down," or use arrow keys.
* **Shoot:** Say "fire," or press `Space`.
* **Levels:** Say "level one," "level two," etc., or select from menu.
* **Power-up:** health, shield, rapid (automatically collected)

---

## 📝 File Structure

```
galactic-fighter/
│
├── final.py
├── voice_control.py
├── sounds/
│ └─ explosion.wav
├── models/
│ └─ vosk-model-small-en-us-0.15/
├── assets/
│ ├─ background.jpg
│ ├─ ship.png
│ └─ power-up.png
├── requirements.txt
├── README.md
```

---

## 🛠 Customize

* To **adjust difficulty**, change `wave_length` or `enemy_vel`.
* To **add more power-ups or enemies**, simply create additional subclasses in `game_classes`.

---

## 🔹 Notes

✅ The game uses **Vosk's small English model for faster, lightweight voice recognition**.
✅ The recognizer runs in a separate thread to avoid blocking the main game loop.

---

## 🐛 Troubleshooting

➥ If you find your voice controls laggy or unreliable:

* Try a quieter room.
* Use a headset.
* Reduce background noise.

➥ If you get an `ImportError` or `ModuleNotFoundError`:

* Make sure you installed all requirements and downloaded the Vosk model.

---
![Screenshot 1](screenshots/s%20(1).png)
![Screenshot 2](screenshots/s%20(2).png)
![Screenshot 3](screenshots/s%20(3).png)
![Screenshot 4](screenshots/s%20(4).png)
## 🙏 Credits

* **OpenAI GPT-4:** Assistance with coding
* **Vosk:** Speech recognition
* **Pygame:** Gaming framework

---

