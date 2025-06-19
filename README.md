# ✨ AI Canvas Interpreter

An intelligent, full-screen canvas web app where you can **draw anything** — math equations, physics diagrams, chemistry molecules, or real-world objects — and get AI-powered answers in real-time using **Gemini Vision** through **LangChain**.

> 🖊️ Powered by LangChain, Streamlit, Gemini Pro Vision, and magic-level UX inspired by Apple’s Math Notes.

---

## 🚀 Features

### 🎨 Interactive AI Drawing Canvas
- Draw freely using a stylus, mouse, or finger (touch-enabled)
- Clean **black canvas** interface with minimal distractions
- Fullscreen drawing space, no scroll required

### ✍️ Pen & Eraser Tools
- Toggle between ✏️ Pen and 🧽 Eraser instantly
- Color picker for custom drawing colors
- Pen size slider for precision control

### 🧠 Real-Time AI Understanding (Gemini Vision)
- Automatically interprets:
  - 🧮 Math problems (algebra, geometry, calculus)
  - 🔬 Physics diagrams (motion, forces, circuits)
  - 🧪 Chemistry structures or labels
  - 🌳 Real-world objects (e.g., tree, lamp, phone)
- Uses Gemini via LangChain to generate accurate explanations, answers, or classifications

### 💬 Instant Feedback with Enter Key
- Just draw and hit **Enter** (or click 🚀 Solve)
- Get the answer **right below the canvas** without scrolling

### 🧹 One-Tap Clear
- Quickly reset the canvas without reloading the app

---

## 🔧 Technologies Used

| Tool                | Purpose                            |
|---------------------|-------------------------------------|
| [Streamlit](https://streamlit.io)        | Frontend & UI rendering               |
| [LangChain](https://www.langchain.com)   | LLM integration framework             |
| [Gemini Pro Vision](https://ai.google.dev) | Multimodal AI (image + text)         |
| `streamlit-drawable-canvas`              | Drawing and annotation canvas         |
| `Pillow` + `base64`                      | Canvas-to-image processing            |

---
## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-canvas-interpreter.git
cd ai-canvas-interpreter
````

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** Dependencies include:
>
> * `streamlit`
> * `streamlit-drawable-canvas`
> * `langchain`
> * `langchain-google-genai`
> * `python-dotenv`
> * `pillow`

### 4. Add your Gemini API Key

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

You can get the key from: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

### 5. Run the app

```bash
streamlit run app.py
```

Then open in your browser at `http://localhost:8501`

---

## 📚 Use Cases

| Scenario              | Example Drawing              | Gemini Response        |
| --------------------- | ---------------------------- | ---------------------- |
| Math Solver           | `x^2 - 4x + 4 = 0`           | Quadratic solution     |
| Physics Diagram       | A falling object with arrows | Time, velocity, energy |
| Chemistry Structure   | H₂O molecule diagram         | Naming + bonds         |
| Object Classification | Drawing of a tree            | “That’s a mango tree”  |

---

## 🔮 Planned Features

* 🧾 Export drawing + answer as PDF or image
* 🧪 Chemistry 3D molecule viewer
* 📊 Graph/simulation for physics
* ✍️ Handwritten OCR + text label detection
* 🧠 AI-powered quiz from drawing

---

## 🙋‍♂️ Author

👨‍💻 **Aditya Padale**
Building smart apps with natural input interfaces.
[GitHub](https://github.com/adityapadale)

---
