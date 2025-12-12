# import streamlit as st
# import requests
# import subprocess

# st.title("AGENTIC BASED PPT GENERATOR")

# prompt= st.text_area("please write the details how you want to create the ppt")

# if st.button("generate ppt"):
#     if prompt:
#         response= requests.post(url="https://ruchi123.app.n8n.cloud/webhook-test/5738f0a1-c841-4fa3-8a77-7df708193621", 
#                                 json={"prompt":prompt})
        
#         if response.status_code== 200:
#             st.write("success")
            
#             with open("app1.py", "w") as file:
                
#                 file.write(response.json()["output"].strip("```python"))
                
#             subprocess.run(["python", "app1.py"])
            

# with open(r"D:\Innomatics\Agentic AI Internship\N8N assignments\PPT Generator\power\presentation.pptx","rb") as f1:
#     st.download_button(
#         label="Download pptx file",
#         data= f1,
#         file_name="data.pptx")            












import streamlit as st
import requests
import subprocess
import time
import os
from datetime import datetime
import json

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="SlideFlow AI – PPT Generator",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- THEME-AWARE CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

/* Brand accents (stable for all themes) */
:root {
    --brand-primary: #6366f1;
    --brand-secondary: #8b5cf6;
    --brand-accent: #ec4899;
    --brand-success: #10b981;
}

/* Reset + base */
* {
    font-family: 'Inter', sans-serif;
    box-sizing: border-box;
}

/* Use Streamlit theme colors so it works in light & dark */
html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--background-color);
}

/* Hide default Streamlit menu/footer if you want a cleaner look */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* HERO HEADER */
.hero-header {
    background: linear-gradient(
        135deg,
        var(--brand-primary) 0%,
        var(--brand-secondary) 45%,
        var(--brand-accent) 100%
    );
    color: white;
    padding: 2rem 2.5rem;
    border-radius: 22px;
    margin-bottom: 1.6rem;  /* slightly tighter */
    box-shadow: 0 18px 35px rgba(0,0,0,0.30);
}

.hero-title {
    font-family: 'Poppins', sans-serif;
    font-size: 2.4rem;
    font-weight: 700;
    margin-bottom: 0.4rem;
}

.hero-subtitle {
    font-size: 1.05rem;
    opacity: 0.96;
    margin-bottom: 0.7rem;
}

.hero-tagline {
    font-size: 0.95rem;
    opacity: 0.90;
}

/* CARDS (default) */
.card {
    background-color: var(--secondary-background-color);
    border-radius: 18px;
    padding: 1.7rem 1.8rem;
    border: 1px solid var(--border-color);
    box-shadow: 0 6px 18px rgba(0,0,0,0.18);
    margin-bottom: 1.0rem;   /* a bit smaller overall */
    transition: box-shadow 0.25s ease, transform 0.15s ease, border-color 0.25s ease;
}
.card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 28px rgba(0,0,0,0.32);
    border-color: var(--primary-color);
}

/* MAIN INPUT CARD: extra tight spacing */
.card-main {
    padding: 1.4rem 1.6rem;
    margin-bottom: 0.35rem;   /* key change: bring button closer */
}

.card-header {
    font-family: 'Poppins', sans-serif;
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--text-color);
    margin-bottom: 1.1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* TEXTAREAS & INPUTS (use theme colors) */
textarea, input, select {
    background-color: var(--background-color) !important;
    color: var(--text-color) !important;
    border-radius: 10px !important;
}

/* METRICS */
.metric-card {
    background-color: var(--secondary-background-color);
    border-radius: 14px;
    border: 1px solid var(--border-color);
    padding: 1.3rem 1.1rem;
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
}
.metric-value {
    font-family: 'Poppins', sans-serif;
    font-size: 1.7rem;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 0.2rem;
}
.metric-label {
    font-size: 0.88rem;
    color: var(--text-color);
    opacity: 0.75;
}

/* TIPS */
.tips-section {
    background: linear-gradient(
        135deg,
        rgba(99,102,241,0.08),
        rgba(139,92,246,0.06)
    );
    border-left: 4px solid var(--primary-color);
    padding: 1.0rem 1.1rem;
    border-radius: 12px;
    margin-top: 0.6rem;
}
.tips-section h4 {
    font-family: 'Poppins', sans-serif;
    font-size: 0.98rem;
    margin-bottom: 0.6rem;
    color: var(--primary-color);
}
.tips-section ul {
    list-style: none;
    padding-left: 0;
    margin: 0;
}
.tips-section li {
    position: relative;
    padding-left: 1.3rem;
    margin-bottom: 0.45rem;
    font-size: 0.9rem;
    color: var(--text-color);
    opacity: 0.85;
}
.tips-section li:before {
    content: "✓";
    position: absolute;
    left: 0;
    top: 0;
    color: var(--brand-success);
    font-weight: 600;
}

/* FEATURES */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 1.0rem;
}
.feature-box {
    background-color: var(--secondary-background-color);
    border-radius: 14px;
    padding: 1.0rem 0.9rem;
    border: 1px solid var(--border-color);
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.feature-box:hover {
    transform: translateY(-3px);
    border-color: var(--primary-color);
    box-shadow: 0 10px 24px rgba(0,0,0,0.26);
}
.feature-icon {
    font-size: 1.9rem;
    margin-bottom: 0.4rem;
}
.feature-title {
    font-family: 'Poppins', sans-serif;
    font-size: 0.98rem;
    font-weight: 600;
    margin-bottom: 0.2rem;
    color: var(--text-color);
}
.feature-desc {
    font-size: 0.86rem;
    color: var(--text-color);
    opacity: 0.78;
}

/* BUTTONS: use Streamlit primary color so they adapt */
.stButton > button {
    background: linear-gradient(
        135deg,
        var(--primary-color),
        #4338ca
    );
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.85rem 1.2rem;
    font-size: 1rem;
    font-weight: 600;
    font-family: 'Poppins', sans-serif;
    box-shadow: 0 6px 18px rgba(0,0,0,0.30);
    transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 26px rgba(0,0,0,0.35);
    filter: brightness(1.03);
}
.stButton > button:focus {
    outline: 2px solid rgba(255,255,255,0.7);
}

/* FOOTER */
.footer {
    text-align: center;
    color: var(--text-color);
    opacity: 0.7;
    font-size: 0.9rem;
    margin-top: 1.8rem;
    padding: 1.4rem 0 0.7rem;
    border-top: 1px solid var(--border-color);
}

/* Responsive */
@media (max-width: 768px) {
    .hero-header {
        padding: 1.6rem;
    }
    .hero-title {
        font-size: 1.9rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if "generated_presentations" not in st.session_state:
    st.session_state.generated_presentations = 0
if "last_generated_time" not in st.session_state:
    st.session_state.last_generated_time = "-"

# ---------- HERO SECTION ----------
st.markdown(
    """
    <div class="hero-header">
        <div class="hero-title">✨ SlideFlow AI</div>
        <div class="hero-subtitle">Turn any idea into a professional PowerPoint in seconds.</div>
        <div class="hero-tagline">Describe your topic • Generate with AI • Download and present.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- MAIN LAYOUT ----------
left, right = st.columns([3, 1], gap="large")

with left:
    st.markdown('<div class="card card-main">', unsafe_allow_html=True)
    st.markdown('<div class="card-header">📝 Describe your presentation</div>', unsafe_allow_html=True)

    prompt = st.text_area(
        label="Presentation details",
        value=st.session_state.get("prompt_input", ""),
        height=210,
        placeholder=(
            "Example: Create a 10‑slide presentation about Machine Learning for college students. "
            "Include: introduction, key concepts, real‑world examples, benefits, and conclusion. "
            "Use simple language and a modern, minimal design."
        ),
        key="prompt_input",
    )
    
# ---------- GENERATE BUTTON (close to card) ----------
st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
btn_col, _ = st.columns([2, 1])
with btn_col:
    generate_clicked = st.button("🎨 Generate presentation", use_container_width=True)

    st.markdown(
        """
        <div class="tips-section">
            <h4>💡 Pro tips for best results</h4>
            <ul>
                <li>Mention the <strong>number of slides</strong> you want.</li>
                <li>Specify the <strong>audience</strong> (students, executives, non‑technical, etc.).</li>
                <li>List key <strong>sections</strong> to include (intro, use‑cases, FAQ, etc.).</li>
                <li>Tell the AI about <strong>tone & style</strong> (formal, casual, storytelling).</li>
                <li>Add any <strong>design hints</strong> (dark theme, corporate, minimal, colorful).</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-header">📊 Generator stats</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-value">{st.session_state.generated_presentations}</div>
                <div class="metric-label">Presentations</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-value">{st.session_state.last_generated_time}</div>
                <div class="metric-label">Last run</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- FEATURES STRIP ----------
st.markdown("---")
st.markdown(
    """
    <div class="feature-grid">
        <div class="feature-box">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Fast generation</div>
            <div class="feature-desc">Get a complete PPT in seconds instead of hours.</div>
        </div>
        <div class="feature-box">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Audience‑aware</div>
            <div class="feature-desc">Tailor content for students, teams, or leadership.</div>
        </div>
               <div class="feature-box">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">AI‑structured</div>
            <div class="feature-desc">Slides are organized into meaningful sections.</div>
        </div>
        <div class="feature-box">
            <div class="feature-icon">📥</div>
            <div class="feature-title">Download ready</div>
            <div class="feature-desc">Editable PPTX file you can fully customize.</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- GENERATION LOGIC ----------
if generate_clicked:
    if not prompt or not prompt.strip():
        st.warning("Please enter your presentation details before generating.")
    else:
        user_prompt = prompt.strip()
        progress_placeholder = st.empty()
        status_placeholder = st.empty()

        try:
            with progress_placeholder.container():
                progress = st.progress(0)

            with status_placeholder.container():
                st.info("🚀 Connecting to AI workflow...")

            # 1) Call your n8n webhook
            progress.progress(30)
            response = requests.post(
                "https://ruchi123.app.n8n.cloud/webhook-test/5738f0a1-c841-4fa3-8a77-7df708193621",
                json={"prompt": user_prompt},
                timeout=90,
            )

            progress.progress(55)
            if response.status_code != 200:
                progress_placeholder.empty()
                status_placeholder.empty()
                st.error(f"API error: {response.status_code}")
            else:
                with status_placeholder.container():
                    st.info("🧠 Generating PPT code...")

                data = response.json()
                code = data.get("output", "")

                # Clean possible fences around code
                code = (
                    code.replace("```pyhton", "").strip()
                )

                # 2) Save and run the generator script
                with open("app1.py", "w", encoding="utf-8") as f:
                    f.write(code)

                progress.progress(75)
                with status_placeholder.container():
                    st.info("📂 Creating PowerPoint file...")

                # Run the generated script (assumes it writes the PPTX to a known path)
                subprocess.Popen(["python", "app1.py"])

                # Wait a bit for file generation (tune if needed)
                time.sleep(6)

                progress.progress(100)
                progress_placeholder.empty()
                status_placeholder.empty()

                # 3) Download section
                st.success("✅ Presentation generated successfully!")

                st.session_state.generated_presentations += 1
                st.session_state.last_generated_time = datetime.now().strftime("%I:%M %p")

                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown(
                    '<div class="card-header">📥 Download your PPTX</div>',
                    unsafe_allow_html=True,
                )

                # IMPORTANT: update this to your actual PPT path
                ppt_path = r"D:\Innomatics\Agentic AI Internship\N8N assignments\PPT Generator\power\presentation.pptx"

                if os.path.exists(ppt_path):
                    with open(ppt_path, "rb") as f:
                        ppt_bytes = f.read()

                    st.download_button(
                        label="📥 Download PPTX",
                        data=ppt_bytes,
                        file_name=f"presentation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx",
                        mime=(
                            "application/vnd.openxmlformats-officedocument."
                            "presentationml.presentation"
                        ),
                        use_container_width=True,
                    )

                    c1, c2, c3 = st.columns(3)
                    with c1:
                        st.metric("File format", "PPTX")
                    with c2:
                        size_kb = os.path.getsize(ppt_path) / 1024
                        st.metric("Size", f"{size_kb:.1f} KB")
                    with c3:
                        st.metric("Status", "Ready")
                else:
                    st.warning(
                        "The PPT generator script ran, but the PPTX file "
                        "was not found at the expected path. Please verify the path."
                    )

                st.markdown("</div>", unsafe_allow_html=True)

        except requests.Timeout:
            progress_placeholder.empty()
            status_placeholder.empty()
            st.error("⏱️ The request to the AI workflow timed out. Please try again.")
        except json.JSONDecodeError:
            progress_placeholder.empty()
            status_placeholder.empty()
            st.error("❌ Could not parse the AI response. Check your n8n output format.")
        except Exception as e:
            progress_placeholder.empty()
            status_placeholder.empty()
            st.error(f"❌ An unexpected error occurred: {e}")

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown(
        """
        <div class="card">
            <div class="card-header">🚀 How it works</div>
            <ol style="padding-left:1.1rem; margin-bottom:0;">
                <li>Describe your topic and audience.</li>
                <li>Click <strong>Generate presentation</strong>.</li>
                <li>Wait a few seconds while AI builds the PPT.</li>
                <li>Download the PPTX and customize if needed.</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card">
            <div class="card-header">💡 Example prompts</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    example_prompts = [
        "Create a 5-slide pitch deck for a food delivery startup with intro, problem, solution, business model, and call-to-action.",
        "Generate 8 slides explaining the basics of Python programming for complete beginners with simple examples.",
        "Make a 6-slide training presentation on data science lifecycle with real-world examples and best practices.",
    ]

    for i, ex in enumerate(example_prompts, start=1):
        if st.button(f"📋 Use example {i}", key=f"ex_{i}", use_container_width=True):
            st.session_state.prompt_input = ex
            st.experimental_rerun()

# ---------- FOOTER ----------
st.markdown(
    """
    <div class="footer">
        <p><strong>SlideFlow AI</strong> · Built with Streamlit & AI</p>
        <p style="font-size:0.8rem; opacity:0.65;">Describe -  Generate -  Download -  Present</p>
    </div>
    """,
    unsafe_allow_html=True,
)

