import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Shane Adrian C. Opinion - Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simple, clean CSS styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css');
    
    * {
        transition: all 0.2s ease;
    }
    
    /* Main background */
    .main {
        padding-top: 2rem;
        background: linear-gradient(135deg, #EDE8F5 0%, #ADBBDA 50%, #EDE8F5 100%);
        background-attachment: fixed;
        min-height: 100vh;
    }
    
    /* Headers */
    h1 {
        color: #3D52A0;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 2.5rem;
        letter-spacing: 0.5px;
        margin-bottom: 1.5rem;
    }
    
    h2 {
        color: #3D52A0;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-left: 4px solid #7091E6;
        padding-left: 1rem;
    }
    
    h3 {
        color: #7091E6;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1.2rem;
    }
    
    h4 {
        color: #8697C4;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1rem;
    }
    
    /* Cards */
    .card {
        background: linear-gradient(135deg, #ffffff 0%, #F5F3FA 100%);
        border: 1px solid #ADBBDA;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        background: linear-gradient(135deg, #F5F3FA 0%, #EDE8F5 100%);
        border-color: #7091E6;
        transform: translateY(-4px);
        box-shadow: 0 10px 25px rgba(61, 82, 160, 0.15);
    }
    
    .card-faith {
        border-color: #7091E6;
        background: linear-gradient(135deg, #F0ECFF 0%, #E8E4F7 100%);
    }
    
    .card-faith:hover {
        background: linear-gradient(135deg, #E8E4F7 0%, #EDE8F5 100%);
        border-color: #3D52A0;
    }
    
    .card-tech {
        border-color: #8697C4;
        background: linear-gradient(135deg, #F5F3FA 0%, #EDE8F5 100%);
    }
    
    .card-tech:hover {
        background: linear-gradient(135deg, #EDE8F5 0%, #ADBBDA 100%);
        border-color: #7091E6;
    }
    
    .card p {
        color: #3D52A0;
        line-height: 1.6;
    }
    
    /* Text */
    p {
        color: #5A5A7A;
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
        line-height: 1.7;
    }
    
    /* Metrics */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #ffffff 0%, #F5F3FA 100%);
        border: 1px solid #ADBBDA;
        border-radius: 10px;
        padding: 1.5rem;
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        background: linear-gradient(135deg, #3D52A0 0%, #7091E6 100%);
        color: #ffffff;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.3rem 0.5rem;
        border: 1px solid #7091E6;
    }
    
    .badge:hover {
        background: linear-gradient(135deg, #7091E6 0%, #8697C4 100%);
        color: #ffffff;
        transform: scale(1.05);
    }
    
    .badge-tech {
        background: linear-gradient(135deg, #7091E6 0%, #8697C4 100%);
        border-color: #8697C4;
    }
    
    .badge-faith {
        background: linear-gradient(135deg, #3D52A0 0%, #7091E6 100%);
        border-color: #7091E6;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #3D52A0 0%, #7091E6 100%);
        color: #ffffff;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #7091E6 0%, #8697C4 100%);
        color: #ffffff;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(61, 82, 160, 0.3);
    }
    
    /* Inputs */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        background: #ffffff !important;
        border: 1px solid #ADBBDA !important;
        color: #3D52A0 !important;
        border-radius: 8px !important;
        padding: 0.8rem !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #7091E6 !important;
        box-shadow: 0 0 10px rgba(112, 145, 230, 0.2) !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #ffffff 0%, #F5F3FA 100%);
        border: 1px solid #ADBBDA;
        border-radius: 8px;
        padding: 1rem;
        color: #3D52A0;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, #F5F3FA 0%, #EDE8F5 100%);
        border-color: #7091E6;
    }
    
    /* Tabs */
    [data-testid="stTab"] {
        color: #8697C4;
        font-weight: 600;
        padding: 0.8rem 1.5rem;
    }
    
    [data-testid="stTab"]:hover {
        color: #7091E6;
    }
    
    [data-testid="stTab"][aria-selected="true"] {
        color: #3D52A0;
        border-bottom: 3px solid #3D52A0;
    }
    
    /* Links */
    a {
        color: #3D52A0;
        text-decoration: none;
        transition: all 0.2s ease;
    }
    
    a:hover {
        color: #7091E6;
        text-decoration: underline;
    }
    
    /* Alert */
    .stAlert {
        background: linear-gradient(135deg, #F0ECFF 0%, #EDE8F5 100%);
        border: 1px solid #ADBBDA;
        border-radius: 10px;
        border-left: 4px solid #7091E6;
        padding: 1rem;
    }
    
    .stAlert > div {
        color: #3D52A0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar */
    .stSidebar {
        background: linear-gradient(180deg, #F5F3FA 0%, #EDE8F5 100%);
        border-right: 1px solid #ADBBDA;
    }
    
    .stSidebar h1 {
        font-size: 1.5rem;
        color: #3D52A0;
    }
    
    .stSidebar .stMarkdown {
        color: #5A5A7A;
    }
    
    /* Sidebar navigation (radio) */
    .stSidebar [data-testid="stRadio"] [role="radiogroup"] {
        display: grid;
        gap: 6px;
        margin-top: 6px;
    }
    
    .stSidebar [data-testid="stRadio"] [role="radio"] {
        border: 1px solid #ADBBDA;
        border-radius: 10px;
        padding: 10px 12px;
        cursor: pointer;
        background: linear-gradient(180deg, #ffffff 0%, #F5F3FA 100%);
        transition: transform 120ms ease, background 220ms ease, border-color 220ms ease, box-shadow 220ms ease;
        animation: st-fade-slide-in 240ms ease both;
    }
    
    .stSidebar [data-testid="stRadio"] [role="radio"]:hover {
        transform: translateX(3px);
        border-color: #7091E6;
        box-shadow: 0 8px 18px rgba(61, 82, 160, 0.15);
        background: linear-gradient(180deg, #F5F3FA 0%, #EDE8F5 100%);
    }
    
    .stSidebar [data-testid="stRadio"] [role="radio"][aria-checked="true"] {
        background: linear-gradient(135deg, #3D52A0 0%, #7091E6 100%);
        border-color: #3D52A0;
        box-shadow: 0 10px 22px rgba(61, 82, 160, 0.25);
    }
    
    .stSidebar [data-testid="stRadio"] [role="radio"][aria-checked="true"] p {
        color: #ffffff !important;
        font-weight: 600;
        letter-spacing: 0.2px;
    }
    
    /* Fallback/broader selectors to ensure styles apply across Streamlit versions */
    .stSidebar [role="radiogroup"] > label,
    .stSidebar [role="radiogroup"] > div[role="radio"] {
        border: 1px solid #ADBBDA !important;
        border-radius: 10px !important;
        padding: 10px 12px !important;
        cursor: pointer;
        background: linear-gradient(180deg, #ffffff 0%, #F5F3FA 100%) !important;
        transition: transform 120ms ease, background 220ms ease, border-color 220ms ease, box-shadow 220ms ease !important;
        animation: st-fade-slide-in 240ms ease both;
    }
    .stSidebar [role="radiogroup"] > label:hover,
    .stSidebar [role="radiogroup"] > div[role="radio"]:hover {
        transform: translateX(3px);
        border-color: #7091E6 !important;
        box-shadow: 0 8px 18px rgba(61, 82, 160, 0.15);
        background: linear-gradient(180deg, #F5F3FA 0%, #EDE8F5 100%) !important;
    }
    .stSidebar [role="radiogroup"] [aria-checked="true"] {
        background: linear-gradient(135deg, #3D52A0 0%, #7091E6 100%) !important;
        border-color: #3D52A0 !important;
        box-shadow: 0 10px 22px rgba(61, 82, 160, 0.25);
    }
    .stSidebar [role="radiogroup"] [aria-checked="true"] p {
        color: #ffffff !important;
        font-weight: 600;
        letter-spacing: 0.2px;
    }
    
    @keyframes st-fade-slide-in {
        from { opacity: 0; transform: translateX(-6px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @media (max-width: 480px) {
      .stSidebar [data-testid="stRadio"] [role="radio"] {
          padding: 8px 10px;
          border-radius: 8px;
      }
      .stSidebar [data-testid="stRadio"] p {
          font-size: 0.9rem !important;
      }
    }
    
    /* Sidebar image nudge right slightly */
    .stSidebar [data-testid="stImage"] img {
        margin-left: 47px;
    }
    
    
    
    
    /* Dataframe */
    .stDataFrame {
        background: linear-gradient(135deg, #ffffff 0%, #F5F3FA 100%) !important;
    }
    
    /* Progress */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #3D52A0 0%, #7091E6 100%);
    }
    
    .hero {
        background: linear-gradient(135deg, #ffffff 0%, #F5F3FA 100%);
        border: 1px solid #ADBBDA;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 12px 30px rgba(61, 82, 160, 0.12);
    }
    
    .hero-title {
        color: #3D52A0;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 2.2rem;
        margin: 0 0 0.5rem 0;
        letter-spacing: 0.4px;
    }
    
    .hero-subtitle {
        color: #7091E6;
        font-weight: 600;
        margin: 0 0 1rem 0;
    }
    
    .hero-photo img {
        width: 100%;
        border-radius: 14px;
        border: 1px solid #ADBBDA;
        box-shadow: 0 14px 28px rgba(61, 82, 160, 0.18);
        display: block;
    }
    
    .divider-soft {
        height: 2px;
        background: linear-gradient(90deg, transparent, #ADBBDA, transparent);
        border: none;
        margin: 1rem 0 2rem 0;
    }
    
    .about-hero {
        background: linear-gradient(135deg, #ffffff 0%, #F5F3FA 100%);
        border: 1px solid #ADBBDA;
        border-radius: 16px;
        padding: 1.5rem 2rem;
        box-shadow: 0 12px 30px rgba(61, 82, 160, 0.12);
        margin-bottom: 1rem;
    }
    
    .about-hero h2 {
        margin: 0 0 0.25rem 0;
    }
    
    .chip {
        display: inline-block;
        padding: 0.4rem 0.9rem;
        background: linear-gradient(135deg, #F0ECFF 0%, #EDE8F5 100%);
        border: 1px solid #ADBBDA;
        color: #3D52A0;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.25rem 0.35rem 0.25rem 0;
    }
    
    .about-quote {
        font-style: italic;
        color: #5A5A7A;
        background: linear-gradient(135deg, #ffffff 0%, #F5F3FA 100%);
        border: 1px solid #ADBBDA;
        border-radius: 12px;
        padding: 1rem 1.25rem;
    }
    
    .interest-card {
        display: flex;
        align-items: center;
        gap: 14px;
    }
    
    .interest-icon {
        width: 44px;
        height: 44px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #ffffff;
        font-size: 22px;
        background: linear-gradient(135deg, #3D52A0 0%, #7091E6 100%);
        box-shadow: 0 10px 22px rgba(61, 82, 160, 0.22);
        border: 1px solid #7091E6;
    }
    
    .interest-title {
        margin: 0;
        color: #3D52A0;
    }
    
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 14px;
        margin-top: 8px;
        animation: edu-fade-up 300ms ease both;
    }
    .skill-card {
        background: linear-gradient(135deg, #ffffff 0%, #F5F3FA 100%);
        border: 1px solid #ADBBDA;
        border-radius: 12px;
        padding: 12px 14px;
        box-shadow: 0 8px 20px rgba(61, 82, 160, 0.12);
        transition: transform 120ms ease, box-shadow 200ms ease, border-color 200ms ease;
    }
    .skill-card:hover {
        transform: translateY(-3px);
        border-color: #7091E6;
        box-shadow: 0 12px 24px rgba(61, 82, 160, 0.2);
    }
    .skill-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 10px;
    }
    .skill-icon {
        width: 36px;
        height: 36px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #ffffff;
        font-size: 18px;
        background: linear-gradient(135deg, #3D52A0 0%, #7091E6 100%);
        border: 1px solid #7091E6;
        box-shadow: 0 6px 16px rgba(61, 82, 160, 0.22);
    }
    .skill-name {
        color: #3D52A0;
        font-weight: 700;
    }
    .skill-cat {
        color: #8697C4;
        font-size: 0.85rem;
        margin-top: -2px;
    }
    .skill-bar {
        height: 8px;
        border-radius: 999px;
        background: #E6E8F5;
        border: 1px solid #D5D9EE;
        overflow: hidden;
    }
    .skill-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #3D52A0 0%, #7091E6 100%);
        border-radius: 999px;
        transition: width 600ms ease;
    }
    .skill-meta {
        text-align: right;
        color: #3D52A0;
        font-weight: 600;
        font-size: 0.85rem;
        margin-top: 6px;
    }
    .stProgress > div > div > div { transition: width 600ms ease; }
    .stProgress > div > div > div > div { transition: width 600ms ease; }
    
    /* Education section */
    .edu-panel {
        background: linear-gradient(135deg, #ffffff 0%, #F5F3FA 100%);
        border: 1px solid #ADBBDA;
        border-radius: 16px;
        padding: 1.25rem 1.5rem;
        box-shadow: 0 12px 30px rgba(61, 82, 160, 0.12);
        animation: edu-fade-up 300ms ease both;
    }
    .edu-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
    }
    .edu-item {
        background: linear-gradient(180deg, #ffffff 0%, #F5F3FA 100%);
        border: 1px solid #E0E4F2;
        border-radius: 12px;
        padding: 12px 14px;
        display: flex;
        align-items: center;
        gap: 10px;
        animation: edu-fade-up 360ms ease both;
    }
    .edu-item i {
        color: #3D52A0;
        font-size: 18px;
    }
    .edu-item p {
        margin: 0;
        color: #3D52A0;
        font-weight: 600;
    }
    .edu-chips {
        margin-top: 6px;
    }
    .edu-chip {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        background: linear-gradient(135deg, #EDE8F5 0%, #F5F3FA 100%);
        border: 1px solid #ADBBDA;
        color: #3D52A0;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.25rem 0.35rem 0 0;
        transition: transform 120ms ease;
    }
    .edu-chip:hover { transform: translateY(-2px); }
    .stExpander .stPlotlyChart {
        background: linear-gradient(135deg, #ffffff 0%, #F5F3FA 100%);
        border: 1px solid #ADBBDA;
        border-radius: 12px;
        padding: 8px;
        box-shadow: 0 10px 24px rgba(61, 82, 160, 0.12);
        animation: edu-fade-up 400ms ease both;
    }
    @keyframes edu-fade-up {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @media (max-width: 780px) {
        .edu-grid { grid-template-columns: 1fr; }
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
# Profile Section
try:
    st.sidebar.image("Image/shane.png", width=180)
except Exception:
    st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #F5F3FA 0%, #EDE8F5 100%); 
                border-radius: 10px; padding: 2rem; text-align: center;
                border: 2px solid #ADBBDA;">
    <p style="color: #999; font-size: 0.9rem;">Profile image not found</p>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="text-align: center; padding: 1.5rem 0;">
    <h3 style="color: #3D52A0; margin: 0.5rem 0; font-size: 1.2rem;">Shane Adrian C. Opinion</h3>
    <p style="color: #7091E6; margin: 0; font-weight: 600; font-size: 0.95rem;">Software Developer</p>
    <p style="color: #8697C4; margin: 0.5rem 0; font-size: 0.85rem;">Cebu | Philippines</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

st.sidebar.title("Navigation")
st.sidebar.markdown("")
page = st.sidebar.radio(
    "Select a section:",
    options=[
        "Home",
        "About Me",
        "Education",
        "Technical Skills",
        "Projects",
        "Leadership & Ministry",
        "Goals & Vision",
        "Contact"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Contact Info**

📧 Email: shane.opinion@email.com  
📍 Location: Philippines  
💻 GitHub | LinkedIn
""")

# HOME PAGE
if page == "Home":
    col1, col2 = st.columns([3, 2], gap="large")
    
    with col1:
        st.markdown("""
        <div class="hero">
          <div class="hero-title">Welcome to My Portfolio</div>
          <div class="hero-subtitle">Shane Adrian C. Opinion</div>
          <p style="margin:0 0 0.6rem 0;color:#5A5A7A;">
            BSIT Student • Aspiring Software Developer • Christian Youth Leader
          </p>
          <hr class="divider-soft"/>
          <p style="color:#5A5A7A;">
            I'm a passionate student pursuing a Bachelor of Science in Information Technology, driven by a vision to create meaningful software solutions that impact lives positively. Beyond coding, I'm deeply involved in Christian youth ministry through CCF NxtGen, where I facilitate Bible studies, lead small group discussions, and create resources to inspire and guide young believers.
          </p>
          <div style="margin-top:0.8rem;">
            <span class="badge">BSIT Student</span>
            <span class="badge badge-tech">Java</span>
            <span class="badge badge-tech">Spring Boot</span>
            <span class="badge badge-tech">React</span>
          </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### My Mission")
        st.markdown("""
        To become a software developer who builds applications that serve a greater purpose—
        combining technical excellence with a heart for serving others and glorifying God
        through meaningful, impactful work.
        """)
    
    with col2:
        st.image("Image/Shane.jpg")
        st.markdown("### Quick Stats")
        metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
        with metrics_col1:
            st.metric(label="Current Year", value="3rd Year", delta="BSIT Program")
        with metrics_col2:
            st.metric(label="Active Projects", value="5+", delta="In Progress")
        with metrics_col3:
            st.metric(label="Years in Ministry", value="4+", delta="CCF NxtGen")
    
    st.markdown("---")
    
    st.markdown("### Key Highlights")
    
    highlight_cols = st.columns(3)
    
    with highlight_cols[0]:
        st.markdown("""
        <div class="card">
        <h3>Full-Stack Development</h3>
        <p>Building robust applications with Java backend and modern React frontends. 
        Currently exploring Spring Boot for enterprise solutions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with highlight_cols[1]:
        st.markdown("""
        <div class="card card-faith">
        <h3>Youth Ministry Leader</h3>
        <p>Active facilitator in CCF NxtGen, leading Bible studies and creating 
        resources for spiritual growth. Passionate about mentoring young believers.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with highlight_cols[2]:
        st.markdown("""
        <div class="card card-tech">
        <h3>Continuous Learner</h3>
        <p>Exploring emerging technologies like AI/ML while mastering core concepts. 
        Committed to growth in both technical and leadership skills.</p>
        </div>
        """, unsafe_allow_html=True)

# ABOUT ME PAGE
elif page == "About Me":
    st.title("About Me")
    st.markdown("""
    <div class="about-hero">
      <h2 style="color:#3D52A0;">Shane Adrian C. Opinion</h2>
      <p style="color:#7091E6;font-weight:600;margin:0;">BSIT Student • Aspiring Software Developer • Christian Youth Leader</p>
      <hr class="divider-soft"/>
      <p style="margin:0;color:#5A5A7A;">
      Hello! I'm Shane, a third-year BSIT student from the Philippines who is passionate about software development and Christian youth ministry. My journey blends technical ambition with spiritual commitment, shaping how I build and why I build.
      </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("### My Story")
        st.markdown("""
        <div class="card">
        <p>
        I grew up with a deep curiosity about how things work—both in technology and in faith. This curiosity led me to pursue BSIT, where I've discovered my passion for solving real-world problems through code.
        </p>
        <p>
        My involvement with CCF NxtGen shaped me into a leader who values integrity, service, and community. I believe our technical abilities should be used to bless others.
        </p>
        <div class="about-quote">“Build with excellence, serve with purpose.”</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Core Values")
        values = {
            "Faith": "God-centered living and decision-making",
            "Integrity": "Honest and ethical in all endeavors",
            "Excellence": "Striving for quality in everything I do",
            "Resilience": "Persisting through challenges and setbacks",
            "Growth": "Continuous learning and self-improvement",
            "Service": "Using my gifts to help others"
        }
        chips = " ".join([f"<span class='chip'>{k}</span>" for k in values.keys()])
        st.markdown(f"{chips}", unsafe_allow_html=True)
        for value, description in values.items():
            st.markdown(f"- **{value}** — {description}")
    
    st.markdown("---")
    
    st.markdown("### Interests & Hobbies")
    
    interest_cols = st.columns(3)
    
    interests = [
        ("ri-code-s-slash-line", "Tech & Programming", "Exploring new frameworks and building projects"),
        ("ri-book-2-line", "Bible & Theology", "Deep dives into Scripture and spiritual topics"),
        ("ri-gamepad-line", "Gaming", "Strategy games and indie game development interest"),
        ("ri-music-2-line", "Music", "Appreciating various genres, especially worship music"),
        ("ri-pencil-line", "Writing", "Creating devotionals, guides, and technical articles"),
        ("ri-team-line", "Community", "Building relationships and mentoring others")
    ]
    
    for idx, (icon, title, desc) in enumerate(interests):
        with interest_cols[idx % 3]:
            st.markdown(f"""
            <div class="card interest-card">
              <div class="interest-icon"><i class="{icon}"></i></div>
              <div>
                <h4 class="interest-title">{title}</h4>
                <p>{desc}</p>
              </div>
            </div>
            """, unsafe_allow_html=True)

# EDUCATION PAGE
elif page == "Education":
    st.title("Educational Background")
    
    st.markdown("### Bachelor of Science in Information Technology (BSIT)")
    
    with st.expander("Program Overview", expanded=True):
        col1, col2 = st.columns(2, gap="large")
        
        with col1:
            focus_areas = ["Web Development", "Software Development", "Database Management", "IT Project Management"]
            chips = " ".join([f"<span class='edu-chip'>{fa}</span>" for fa in focus_areas])
            st.markdown(f"""
            <div class="edu-panel">
              <div class="edu-grid">
                <div class="edu-item">
                  <i class="ri-graduation-cap-line"></i>
                  <p>Current Status: 3rd Year Student</p>
                </div>
                <div class="edu-item">
                  <i class="ri-calendar-event-line"></i>
                  <p>Expected Graduation: 2025/2026</p>
                </div>
              </div>
              <div style="margin-top:10px;">
                <p style="margin:0 0 6px 0;color:#3D52A0;font-weight:700;">Focus Areas</p>
                <div class="edu-chips">{chips}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            fig_education = go.Figure(data=[
                go.Bar(y=['Year 1', 'Year 2', 'Year 3'], 
                       x=[4.0, 3.8, 3.9],
                       orientation='h',
                       marker_color='#7091E6')
            ])
            fig_education.update_layout(
                title="GPA Progression",
                xaxis_title="GPA",
                yaxis_title="Academic Year",
                showlegend=False,
                height=300
            )
            st.plotly_chart(fig_education, use_container_width=True)
    
    st.markdown("---")
    
    st.markdown("### Key Subjects & Learning")
    
    subjects = {
        "Programming": ["Object-Oriented Programming (Java)", "Data Structures & Algorithms", "Web Development"],
        "Backend": ["Database Design (SQL)", "Spring Boot Framework", "API Development"],
        "Frontend": ["HTML, CSS, JavaScript", "React.js Framework", "Responsive Design"],
        "Core IT": ["Computer Networks", "Information Systems", "IT Project Management"],
        "Emerging": ["Artificial Intelligence Concepts", "Machine Learning Basics", "Mobile Development"]
    }
    
    cols = st.columns(2)
    
    for idx, (category, subject_list) in enumerate(subjects.items()):
        with cols[idx % 2]:
            st.markdown(f"**{category}**")
            for subject in subject_list:
                st.markdown(f"- {subject}")
            st.markdown("")

# TECHNICAL SKILLS PAGE
elif page == "Technical Skills":
    st.title("Technical Skills")
    
    st.markdown("""
    A comprehensive overview of my technical expertise, developed through coursework,
    personal projects, and continuous self-learning.
    """)
    
    skills_data = {
        "Skill": [
            "Java", "Spring Boot", "React.js", "JavaScript", 
            "SQL", "MySQL", "HTML/CSS", "Git",
            "API Development", "REST", "Object-Oriented Design", "Data Structures",
            "AI Concepts", "Python Basics", "MVC Architecture", "Problem Solving"
        ],
        "Category": [
            "Backend", "Backend", "Frontend", "Frontend",
            "Database", "Database", "Frontend", "Tools",
            "Backend", "Backend", "Concepts", "Concepts",
            "Emerging", "Emerging", "Architecture", "Concepts"
        ],
        "Proficiency": [90, 75, 85, 80, 85, 80, 90, 95, 80, 85, 85, 90, 60, 65, 80, 90]
    }
    
    df_skills = pd.DataFrame(skills_data)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("### Skills by Category")
        
        category_skills = df_skills.groupby("Category")["Proficiency"].mean().sort_values(ascending=False)
        
        fig = px.pie(
            values=category_skills.values,
            names=category_skills.index,
            title="Skills Distribution",
            color_discrete_sequence=['#3D52A0', '#7091E6', '#8697C4', '#ADBBDA']
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Average Proficiency by Category")
        
        for category in category_skills.index:
            level = category_skills[category]
            st.markdown(f"**{category}**: {level:.0f}%")
            st.progress(level / 100)
    
    icon_map = {
        "Backend": "ri-server-line",
        "Frontend": "ri-layout-2-line",
        "Database": "ri-database-2-line",
        "Tools": "ri-tools-line",
        "Concepts": "ri-lightbulb-flash-line",
        "Emerging": "ri-rocket-2-line",
        "Architecture": "ri-building-4-line"
    }
    cards_html = []
    for _, row in df_skills.sort_values("Proficiency", ascending=False).iterrows():
        skill = row["Skill"]
        cat = row["Category"]
        prof = int(row["Proficiency"])
        icon = icon_map.get(cat, "ri-star-line")
        card = (
            f'<div class="skill-card">'
            f'<div class="skill-header">'
            f'<div class="skill-icon"><i class="{icon}"></i></div>'
            f'<div><div class="skill-name">{skill}</div><div class="skill-cat">{cat}</div></div>'
            f'</div>'
            f'<div class="skill-bar"><div class="skill-bar-fill" style="width:{prof}%"></div></div>'
            f'<div class="skill-meta">{prof}%</div>'
            f'</div>'
        )
        cards_html.append(card)
    st.markdown("### Skill Cards")
    skills_html = '<div class="skills-grid">' + ''.join(cards_html) + '</div>'
    st.markdown(skills_html, unsafe_allow_html=True)

# PROJECTS PAGE
elif page == "Projects":
    st.title("Projects & Portfolio")
    
    st.markdown("""
    A showcase of my work, ranging from academic projects to personal endeavors.
    Each project represents my growth as a developer and commitment to excellence.
    """)
    
    project_type = st.selectbox(
        "Filter by category:",
        ["All", "Academic", "Full-Stack", "React Games", "Spring Boot", "Capstone"]
    )
    
    projects = [
        {
            "title": "E-Commerce CRUD System",
            "category": "Spring Boot",
            "description": "A complete CRUD application built with Spring Boot for managing products in an online store.",
            "technologies": ["Java", "Spring Boot", "MySQL", "REST API"],
            "date": "2024"
        },
        {
            "title": "Student Information System",
            "category": "Full-Stack",
            "description": "Full-stack application combining Java backend with React frontend for managing student records.",
            "technologies": ["Java", "React.js", "MySQL", "API"],
            "date": "2024"
        },
        {
            "title": "Tic-Tac-Toe Game",
            "category": "React Games",
            "description": "Interactive React game with AI opponent and responsive design.",
            "technologies": ["React", "JavaScript", "CSS"],
            "date": "2023"
        },
        {
            "title": "Quiz Game Application",
            "category": "React Games",
            "description": "Educational quiz game with scoring system and multiple difficulty levels.",
            "technologies": ["React", "JavaScript", "Hooks"],
            "date": "2024"
        },
        {
            "title": "Library Management System",
            "category": "Academic",
            "description": "Comprehensive system for managing library operations and patron records.",
            "technologies": ["Java", "SQL", "Data Structures"],
            "date": "2023"
        },
        {
            "title": "Budget Tracker App",
            "category": "Full-Stack",
            "description": "Web application for personal finance management and expense tracking.",
            "technologies": ["React", "Node.js", "MongoDB"],
            "date": "2024"
        },
        {
            "title": "Capstone - Community Help Hub",
            "category": "Capstone",
            "description": "Proposed platform connecting community members seeking help with volunteers willing to assist.",
            "technologies": ["Full-Stack", "React", "Spring Boot", "MySQL", "AI Matching"],
            "date": "In Development"
        }
    ]
    
    if project_type != "All":
        filtered_projects = [p for p in projects if p["category"] == project_type]
    else:
        filtered_projects = projects
        
    for idx, project in enumerate(filtered_projects):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"""
            <div class="card">
            <h3>{project['title']}</h3>
            <p><strong>Category:</strong> {project['category']} | <strong>Date:</strong> {project['date']}</p>
            <p>{project['description']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("**Tech Stack:**")
            for tech in project['technologies']:
                st.markdown(f'<span class="badge badge-tech">{tech}</span>', unsafe_allow_html=True)

# LEADERSHIP & MINISTRY PAGE
elif page == "Leadership & Ministry":
    st.title("Leadership & Ministry Experience")
    
    st.markdown("""
    My involvement in CCF NxtGen (Christ's Commission Fellowship - Young Adults/NextGen) 
    has been transformative. It's where I've developed my leadership skills while growing spiritually.
    """)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("### Ministry Involvement")
        
        metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
        
        with metrics_col1:
            st.metric("Years Involved", "4+")
        
        with metrics_col2:
            st.metric("Bible Studies Led", "20+")
        
        with metrics_col3:
            st.metric("Small Groups Facilitated", "15+")
    
    with col2:
        st.markdown("### My Roles in CCF NxtGen")
        
        st.markdown("""
        - **Bible Study Facilitator** - Leading deep dives into Scripture
        - **Small Group Leader** - Guiding meaningful discussions
        - **Worship Leader** - Leading worship in community gatherings
        - **Mentor** - Discipling newer believers
        - **Event Organizer** - Planning spiritual retreats and activities
        """)
    
    st.markdown("---")
    
    st.markdown("### Ministry Activities")
    
    timeline_items = [
        ("Regular Weekly Bible Studies", "Facilitate engaging Bible study sessions every Friday, exploring topics like faith, discipleship, and Christian living."),
        ("Small Group Discussions", "Lead intimate group discussions tackling real-life issues faced by young believers in today's world."),
        ("Youth-Friendly Devotionals", "Create and share daily devotional guides tailored for young adults, making spiritual growth accessible and relatable."),
        ("Spiritual Retreats", "Organize and facilitate multi-day retreats for spiritual renewal, community building, and deeper discipleship."),
        ("Mentoring & Discipleship", "One-on-one mentoring relationships with younger believers, helping them navigate faith and personal growth."),
        ("Worship & Prayer Events", "Participate in leading worship and organizing prayer meetings to deepen community's spiritual connection."),
    ]
    
    for title, desc in timeline_items:
        st.markdown(f"""
        <div class="card card-faith">
        <h4>{title}</h4>
        <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# GOALS & VISION PAGE
elif page == "Goals & Vision":
    st.title("Goals & Vision")
    
    st.markdown("""
    My journey is driven by clear aspirations that blend technical excellence with spiritual purpose.
    I'm committed to building a career that makes a meaningful difference while honoring my values.
    """)
    
    st.markdown("## Short-Term Goals (Next 1-2 Years)")
    
    short_term = [
        "Graduate with honors in BSIT (Target: GPA 3.8+)",
        "Master Spring Boot and build enterprise-level applications",
        "Complete capstone project (Community Help Hub) with excellence",
        "Contribute to open-source projects",
        "Develop portfolio of full-stack projects",
        "Deepen expertise in one emerging tech (AI/ML or Cloud)"
    ]
    
    cols = st.columns(2)
    for idx, goal in enumerate(short_term):
        with cols[idx % 2]:
            st.markdown(f"<div class='card'><p>✓ {goal}</p></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## Medium-Term Goals (2-5 Years)")
    
    medium_term_data = {
        "Goal": [
            "Land First Developer Position",
            "Build Meaningful Project",
            "Expand Technical Expertise",
            "Lead Development Team",
            "Mentor Others"
        ],
        "Description": [
            "Secure entry-level position at reputable tech company",
            "Create application that genuinely helps community/non-profit",
            "Master multiple frameworks and technologies",
            "Progress to team lead/senior developer role",
            "Guide and develop junior developers"
        ],
        "Timeline": [
            "Year 1-2",
            "Year 2-3",
            "Ongoing",
            "Year 4-5",
            "Year 3+"
        ]
    }
    
    df_medium = pd.DataFrame(medium_term_data)
    st.dataframe(df_medium, use_container_width=True)

# CONTACT PAGE
elif page == "Contact":
    st.title("Get In Touch")
    
    st.markdown("""
    I'd love to hear from you! Whether you're interested in collaboration, mentorship, 
    or just want to chat about tech and faith, feel free to reach out.
    """)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("### Contact Information")
        
        st.markdown("""
        **Shane Adrian C. Opinion**
        
        Email: shane.opinion@email.com  
        Phone: +63 (XXX) XXX-XXXX  
        Location: Philippines  
        GitHub: github.com/shane-opinion  
        LinkedIn: linkedin.com/in/shane-opinion
        """)
        
        st.markdown("---")
        
        st.markdown("### What I'm Looking For")
        
        st.markdown("""
        - Internship or Junior Developer opportunities
        - Mentorship from experienced developers
        - Collaboration on meaningful projects
        - Learning opportunities in Spring Boot and React
        - Speaking opportunities about tech + faith
        - Community building initiatives
        """)
    
    with col2:
        st.markdown("### Contact Form")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.selectbox(
                "Subject",
                [
                    "Collaboration Opportunity",
                    "Mentorship/Advice",
                    "Job/Internship Opportunity",
                    "Project Discussion",
                    "Speaking Engagement",
                    "General Inquiry",
                    "Other"
                ]
            )
            
            message = st.text_area("Your Message", height=150)
            
            submitted = st.form_submit_button("Send Message", use_container_width=True)
            
            if submitted:
                if name and email and message:
                    st.success("Thank you for reaching out! I'll get back to you soon.")
                    st.balloons()
                else:
                    st.error("Please fill in all required fields.")

# Footer
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("**Shane Adrian C. Opinion**  \n*BSIT Student | Aspiring Developer*")

with footer_col2:
    st.markdown("**Quick Links**  \n[GitHub](#) | [LinkedIn](#) | [Email](mailto:shane@example.com)")

with footer_col3:
    st.markdown(f"**Updated:** February 2026  \nBuilt with Streamlit")
