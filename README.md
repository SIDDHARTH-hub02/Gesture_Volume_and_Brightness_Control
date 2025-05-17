# ✋ Controlling Personal Devices Using Air Gestures

A Python-based computer vision project that allows users to control **volume** and **screen brightness** using simple **hand gestures** captured via webcam. This hands-free control system provides a hygienic, intuitive, and accessible interface for users to interact with personal devices.

---

## 📌 Features

- **Volume Control:** Adjust the system volume using the distance between your thumb and index finger (MediaPipe points 4 and 8).
- **Brightness Control:** Change screen brightness using the distance between your thumb and middle finger (MediaPipe points 4 and 12).
- **Real-time Feedback:** Displays gesture and control bar overlays on webcam feed.
- **Hands-Free Interface:** Suitable for accessibility, clean environments, and immersive experiences.

---

## 🧠 How It Works

This project uses a webcam to track hand landmarks using **MediaPipe**. Based on the calculated distance between specific finger landmarks:

- Volume is mapped from the distance between the **thumb and index finger**.
- Brightness is mapped from the distance between the **thumb and middle finger**.

These values are then passed to system-level APIs using:
- `pycaw` for Windows audio control
- `screen_brightness_control` for screen brightness

---

## 📁 Project Structure

```bash
.
├── Brightness and Volume.py   # Main Python script
├── README.md                  # Project description and documentation
└── DT project est.pdf         # Detailed project report and documentation
