import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
import base64
from dotenv import load_dotenv
import os

# Load Gemini API Key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("Please add your GOOGLE_API_KEY to the .env file")
    st.stop()

# LangChain + Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.messages import HumanMessage
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# Streamlit setup
st.set_page_config(page_title="AI Canvas", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
        #MainMenu, header, footer {visibility: hidden;}
        .block-container {padding-top: 0rem; padding-bottom: 0rem;}
        .css-18ni7ap {padding: 0rem 1rem 1rem 1rem;}
        div[data-testid="stCanvasToolbar"] {display: none !important;}
        canvas + div {display: none !important;}
    </style>
""", unsafe_allow_html=True)

# --- Session state initialization ---
if "canvas_key" not in st.session_state:
    st.session_state.canvas_key = "canvas_1"
if "answer" not in st.session_state:
    st.session_state.answer = None
if "enter_trigger" not in st.session_state:
    st.session_state.enter_trigger = False
if "tool_mode" not in st.session_state:
    st.session_state.tool_mode = "pen"
if "pen_color" not in st.session_state:
    st.session_state.pen_color = "#ffffff"
if "stroke_width" not in st.session_state:
    st.session_state.stroke_width = 4

# --- Toolbar ---
col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 2, 1, 1, 3])
with col1:
    if st.button("✏️ Pen"):
        st.session_state.tool_mode = "pen"
with col2:
    if st.button("🧽 Eraser"):
        st.session_state.tool_mode = "eraser"
with col3:
    if st.session_state.tool_mode == "pen":
        st.session_state.pen_color = st.color_picker("✏️ Color", st.session_state.pen_color, label_visibility="collapsed")
with col4:
    st.session_state.stroke_width = st.slider("✏️ Size", 1, 20, st.session_state.stroke_width)
with col5:
    if st.button("🧹 Clear"):
        st.session_state.canvas_key += "_clear"
        st.session_state.answer = None
        st.rerun()
with col6:
    run = st.button("🚀 Solve")

# --- JS for Enter Key Trigger ---
import streamlit.components.v1 as components
components.html("""
    <script>
        const trigger = () => {
            fetch("/_trigger").then(() => window.location.reload());
        }
        window.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                trigger();
            }
        });
    </script>
""", height=0)

# --- Canvas setup ---
stroke_color = "#000000" if st.session_state.tool_mode == "eraser" else st.session_state.pen_color
stroke_width = st.session_state.stroke_width

canvas_result = st_canvas(
    fill_color="rgba(0,0,0,0)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color="#000000",
    height=680,
    width=1400,
    drawing_mode="freedraw",
    key=st.session_state.canvas_key
)

# --- Gemini AI Solve ---
if (run or st.session_state.enter_trigger) and canvas_result.image_data is not None:
    st.session_state.enter_trigger = False

    img = Image.fromarray((canvas_result.image_data).astype("uint8"))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode()

    prompt = (
        "This is a hand-drawn image. It may contain math problems, physics or chemistry questions, or objects like trees. "
        "Interpret the image accurately and provide a solution or clear explanation."
    )

    response = llm.invoke([
        HumanMessage(
            content=[
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}}
            ]
        )
    ])

    st.session_state.answer = response.content.strip()

# --- Display Gemini Answer ---
if st.session_state.answer:
    st.subheader("🧠 Gemini's Answer")
    st.markdown(f"```markdown\n{st.session_state.answer}\n```")

# --- Fun & Beautiful Footer ---
st.markdown(
    '''<div style="text-align:center; margin-top:40px; font-size:18px; color:#888;">
        Made with ☕, code, and a dash of genius by <b>Aditya Padale</b> 😎<br>
        If you enjoyed this, send virtual high-fives or snacks! 🚀✨
    </div>''',
    unsafe_allow_html=True
)
