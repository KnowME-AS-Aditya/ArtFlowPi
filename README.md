# 🎨 ArtFlowPi – AI Virtual Painter with Index Finger Tracking

[![Last Commit](https://img.shields.io/github/last-commit/KnowME-AS-Aditya/ArtFlowPi?color=blue&style=flat-square)](https://github.com/KnowME-AS-Aditya/ArtFlowPi)
[![Repo Stars](https://img.shields.io/github/stars/KnowME-AS-Aditya/ArtFlowPi?style=flat-square)](https://github.com/KnowME-AS-Aditya/ArtFlowPi/stargazers)
[![Languages](https://img.shields.io/github/languages/top/KnowME-AS-Aditya/ArtFlowPi?color=purple&style=flat-square)](https://github.com/KnowME-AS-Aditya/ArtFlowPi)
[![Issues](https://img.shields.io/github/issues/KnowME-AS-Aditya/ArtFlowPi?style=flat-square)](https://github.com/KnowME-AS-Aditya/ArtFlowPi/issues)

---

## 🧠 What is ArtFlowPi?

**ArtFlowPi** is an **AI-powered virtual canvas** that lets users draw using their **index finger tracked via webcam** — no touchscreen or mouse needed!

It uses:
- 🖐️ [MediaPipe](https://google.github.io/mediapipe/) for real-time **hand landmark detection**
- 🎥 OpenCV for webcam & canvas operations
- 🎨 Custom GUI with color palette & eraser
- 🍓 **Raspberry Pi support** for edge-level AI drawing
- 📝 [IEEE Xplore](https://ieeexplore.ieee.org/document/10094385) for references

---

## 🖼️ Project Preview

| 👇 Live Drawing Feed | 🎯 Canvas Output |
|----------------------|------------------|
| ![Image1](./demo.gif) | ![Image2](./canvas_sample.png) |

> 🔁 Replace with actual GIF/screenshot after you record using ShareX or ScreenToGif.

---

## ⚙️ Tech Stack

| Tech        | Role                           |
|-------------|--------------------------------|
| **Python**  | Core programming language      |
| **OpenCV**  | Video capture, canvas overlay  |
| **MediaPipe** | Hand landmark & index tracking |
| **NumPy**   | Canvas manipulation            |
| **Raspberry Pi** | Optional processor platform |

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/KnowME-AS-Aditya/ArtFlowPi.git
cd ArtFlowPi

# Install dependencies
pip install -r requirements.txt

# Run the app
python ArtFlowPi_primary.py
```
⚠️ Requires a webcam or a Raspberry pi cam. Works best on systems with OpenCV + MediaPipe installed.

🎨 Features
Draw using your index finger

Choose between Red, Green, Blue brushes

Use Eraser with fingertip too

Press 'c' to clear the canvas

Press 'q' to exit

📡 Hardware Compatibility
Device	Status :-
 Laptop/Desktop	✅ Fully supported
 Raspberry Pi (3B+)	✅ Tested with webcam
 Jetson Nano	🟡 Experimental
 Android via OTG	🔴 Not supported yet

🛠️ Future Scope
⫸ Add hand gesture-based controls

⫸ Save canvas output as image

⫸ Add brush size and shape options

⫸ Use TFLite for faster Pi inference

⫸ Web version with Flask/Gradio

🙌 Credits
Developed with 💙 by Aditya Ranjan Sahoo


📜 License
This project is licensed under the Apache 2.0 License.
See the LICENSE file for details.

