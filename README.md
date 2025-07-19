# Air Canvas 🎨✋ | Virtual Drawing App using Computer Vision

This project allows you to draw on your screen in real time using **hand gestures** detected via your webcam — no physical contact or stylus required!

Built using **OpenCV** and **MediaPipe**, it turns your finger into a virtual paintbrush to create drawings in the air.

---

## 🧠 Project Overview

- **Objective:** Enable users to draw on a virtual canvas using finger movement tracked by a webcam.
- **Approach:** Use **MediaPipe** to detect hand landmarks and **OpenCV** for real-time drawing.
- **Modes:** Color selection, drawing mode, eraser mode.

---

## 🎯 Features

- Real-time hand tracking using webcam
- Index finger used as a virtual pen
- Virtual color palette for selecting pen color
- Eraser functionality
- Smooth drawing using gesture-based controls

---

## 🧰 Technologies Used

- Python 3.x
- OpenCV
- MediaPipe
- NumPy

---

## 📁 Folder Structure

```
air-canvas-computer-vision/
│
├── air_canvas.py             # Main application file
├── header/                   # Folder containing palette/header images
│   ├── 1.png                 # Red
│   ├── 2.png                 # Green
│   ├── 3.png                 # Blue
│   ├── 4.png                 # Eraser
│   └── ...                   # Add your own images
├── README.md
└── requirements.txt          # Python dependencies
```

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aarya-04/air-canvas-computer-vision.git
   cd air-canvas-computer-vision
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   python air_canvas.py
   ```

4. **Usage Instructions:**
   - Show your hand clearly in front of webcam.
   - Use **index finger** to move the cursor and draw.
   - Use **two fingers** to switch tools or change colors.
   - Hover over color icons at the top to activate them.

---

## 🖼️ Demo

https://github.com/Aarya-04/air-canvas-computer-vision/assets/demo.gif  
*(Add a real demo GIF if possible)*

---

## 🧪 MediaPipe Hand Tracking

- The app uses 21 hand landmarks to identify and track fingers.
- Drawing happens only when the index finger is raised and others are folded.

---

## 📌 Future Enhancements

- Save drawings as images
- Multi-hand support
- Add brush size selection
- Integrate gesture-based undo/redo

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Aarya Kulkarni**  
[LinkedIn](https://www.linkedin.com/in/aaryakulkarni03) • [GitHub](https://github.com/Aarya-04)

---

> “Turning your hand into a brush — draw in the air with AI and Computer Vision.”
