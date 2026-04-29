"""
╔══════════════════════════════════════════════════════════════╗
║         MEDISCAN AI — Disease Prediction System              ║
║         Diabetes | Heart Disease | Parkinson's               ║
╚══════════════════════════════════════════════════════════════╝

Author  : Ashish Balodia
Version : 1.0.0
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib
import json
import os
from pathlib import Path

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MediScan AI | Disease Prediction",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────────────────────
# CUSTOM CSS — Dark Medical Theme
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@700&display=swap');

    * { box-sizing: border-box; }

    .stApp {
        background: #0f1117;
        font-family: 'Inter', sans-serif;
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827 0%, #0f1117 100%);
        border-right: 1px solid #1f2937;
    }
    [data-testid="stSidebar"] .stRadio label {
        color: #9ca3af !important;
        font-size: 14px;
        padding: 10px 16px;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
        border: 1px solid transparent;
    }
    [data-testid="stSidebar"] .stRadio label:hover {
        background: #1f2937;
        color: #f9fafb !important;
    }

    /* ── Typography ── */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #60a5fa, #a78bfa, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 4px;
    }
    .main-subtitle {
        color: #6b7280;
        font-size: 1rem;
        font-weight: 400;
        margin-bottom: 32px;
    }
    h1, h2, h3 { color: #f9fafb; }
    label { color: #d1d5db !important; font-size: 0.88rem !important; font-weight: 500 !important; }

    /* ── Cards ── */
    .stat-card {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        border: 1px solid #374151;
        border-radius: 12px;
        padding: 20px 24px;
        text-align: center;
        transition: transform 0.2s, border-color 0.2s;
    }
    .stat-card:hover { transform: translateY(-2px); border-color: #4b5563; }
    .stat-number { font-size: 2.2rem; font-weight: 700; color: #60a5fa; line-height: 1; }
    .stat-label { font-size: 0.75rem; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 6px; }

    .info-card {
        background: #1f2937;
        border: 1px solid #374151;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .info-card h4 { color: #e5e7eb; font-size: 1rem; font-weight: 600; margin-bottom: 8px; }
    .info-card p { color: #9ca3af; font-size: 0.88rem; line-height: 1.6; }

    /* ── Section Header ── */
    .section-header {
        font-size: 1.1rem;
        font-weight: 600;
        color: #e5e7eb;
        padding: 12px 0 8px 0;
        border-bottom: 1px solid #374151;
        margin-bottom: 20px;
    }

    /* ── Result Boxes ── */
    .result-positive {
        background: linear-gradient(135deg, #7f1d1d22, #991b1b11);
        border: 2px solid #ef4444;
        border-radius: 16px;
        padding: 28px 32px;
        margin: 20px 0;
        text-align: center;
    }
    .result-negative {
        background: linear-gradient(135deg, #14532d22, #15803d11);
        border: 2px solid #22c55e;
        border-radius: 16px;
        padding: 28px 32px;
        margin: 20px 0;
        text-align: center;
    }
    .result-title { font-size: 1.6rem; font-weight: 700; margin-bottom: 6px; }
    .result-positive .result-title { color: #ef4444; }
    .result-negative .result-title { color: #22c55e; }
    .result-subtitle { color: #9ca3af; font-size: 0.9rem; }

    /* ── Confidence Bar ── */
    .confidence-bar-bg {
        background: #1f2937;
        border-radius: 999px;
        height: 8px;
        margin: 16px 0 6px 0;
        overflow: hidden;
    }
    .confidence-bar-fill { height: 100%; border-radius: 999px; }

    /* ── Badges ── */
    .badge { display: inline-block; padding: 3px 10px; border-radius: 999px; font-size: 0.75rem; font-weight: 600; }
    .badge-blue   { background: #1d4ed833; color: #60a5fa; }
    .badge-green  { background: #14532d33; color: #4ade80; }
    .badge-purple { background: #4c1d9533; color: #c084fc; }

    /* ── Button ── */
    .stButton > button {
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 12px 32px;
        font-size: 1rem;
        font-weight: 600;
        width: 100%;
        cursor: pointer;
        transition: opacity 0.2s, transform 0.1s;
        letter-spacing: 0.03em;
    }
    .stButton > button:hover { opacity: 0.9; transform: translateY(-1px); }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] { background: #1f2937; border-radius: 10px; padding: 4px; gap: 4px; }
    .stTabs [data-baseweb="tab"] { border-radius: 8px; color: #9ca3af; font-size: 0.9rem; }
    .stTabs [aria-selected="true"] { background: #2563eb !important; color: white !important; }

    /* ── Disclaimer ── */
    .disclaimer {
        background: #1c1f26;
        border: 1px solid #fbbf2440;
        border-left: 3px solid #fbbf24;
        border-radius: 8px;
        padding: 12px 16px;
        color: #9ca3af;
        font-size: 0.82rem;
        margin-top: 24px;
    }

    /* ── Inputs ── */
    .stNumberInput input, .stSelectbox select {
        background: #1f2937 !important;
        border: 1px solid #374151 !important;
        color: #f9fafb !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────────────────────
BASE_DIR    = Path(__file__).parent
MODELS_DIR  = BASE_DIR / "saved_models"
DATASET_DIR = BASE_DIR / "dataset"


# ─────────────────────────────────────────────────────────────
# MODEL LOADER  (cached for performance)
# ─────────────────────────────────────────────────────────────
@st.cache_resource
def load_model(disease: str):
    model   = joblib.load(MODELS_DIR / f"{disease}_model.pkl")
    scaler  = joblib.load(MODELS_DIR / f"{disease}_scaler.pkl")
    with open(MODELS_DIR / f"{disease}_metrics.json") as f:
        metrics = json.load(f)
    return model, scaler, metrics


def run_prediction(disease: str, features: list):
    model, scaler, metrics = load_model(disease)
    arr   = np.array(features).reshape(1, -1)
    arr_s = scaler.transform(arr)
    pred  = model.predict(arr_s)[0]
    proba = model.predict_proba(arr_s)[0]
    return int(pred), float(proba[1]), metrics


def show_result(pred: int, prob: float, positive_label: str, negative_label: str,
                positive_emoji: str = "⚠️", negative_emoji: str = "✅",
                positive_sub: str = "", negative_sub: str = ""):
    """Render the prediction result card."""
    if pred == 1:
        bar_color = "linear-gradient(90deg,#ef4444,#f97316)"
        conf_val  = prob * 100
        st.markdown(f"""
        <div class="result-positive">
            <div style="font-size:3rem;margin-bottom:8px;">{positive_emoji}</div>
            <div class="result-title">{positive_label}</div>
            <div class="result-subtitle">{positive_sub}</div>
            <div class="confidence-bar-bg">
                <div class="confidence-bar-fill" style="width:{conf_val:.1f}%;background:{bar_color};"></div>
            </div>
            <div style="color:#ef4444;font-weight:700;font-size:1.3rem;">{conf_val:.1f}% Confidence</div>
        </div>""", unsafe_allow_html=True)
    else:
        bar_color = "linear-gradient(90deg,#22c55e,#16a34a)"
        conf_val  = (1 - prob) * 100
        st.markdown(f"""
        <div class="result-negative">
            <div style="font-size:3rem;margin-bottom:8px;">{negative_emoji}</div>
            <div class="result-title">{negative_label}</div>
            <div class="result-subtitle">{negative_sub}</div>
            <div class="confidence-bar-bg">
                <div class="confidence-bar-fill" style="width:{conf_val:.1f}%;background:{bar_color};"></div>
            </div>
            <div style="color:#22c55e;font-weight:700;font-size:1.3rem;">{conf_val:.1f}% Confidence</div>
        </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# SIDEBAR NAVIGATION
# ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center;padding:20px 0 16px 0;'>
        <div style='font-size:2.5rem;'>🏥</div>
        <div style='font-family:"Playfair Display",serif;font-size:1.4rem;font-weight:700;
                    background:linear-gradient(135deg,#60a5fa,#a78bfa);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;'>
            MediScan AI
        </div>
        <div style='color:#6b7280;font-size:0.78rem;margin-top:4px;'>Disease Prediction System</div>
    </div>
    <hr style='border-color:#1f2937;margin:0 0 20px 0;'>
    <p style='color:#6b7280;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:8px;'>NAVIGATION</p>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        [
            "🏠  Home",
            "🩺  Diabetes Prediction",
            "❤️  Heart Disease",
            "🧠  Parkinson's Disease",
            "📊  Model Analytics",
            "ℹ️   About"
        ],
        label_visibility="collapsed"
    )

    st.markdown("""
    <hr style='border-color:#1f2937;margin:20px 0;'>
    <div style='color:#4b5563;font-size:0.75rem;line-height:1.6;'>
        ⚠️ For educational purposes only.<br>
        Consult a qualified physician for medical advice.
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PAGE — HOME
# ══════════════════════════════════════════════════════════════
if page == "🏠  Home":
    st.markdown('<h1 class="main-title">MediScan AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="main-subtitle">AI-powered disease prediction using clinical & voice biomarkers</p>', unsafe_allow_html=True)

    # ── KPI row ──
    c1, c2, c3, c4 = st.columns(4)
    kpis = [
        ("3",      "#60a5fa", "Diseases Covered"),
        ("~99%",   "#a78bfa", "Model Accuracy"),
        ("3,300+", "#34d399", "Training Samples"),
        ("GB",     "#fb923c", "Gradient Boosting"),
    ]
    for col, (num, color, label) in zip([c1,c2,c3,c4], kpis):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number" style="color:{color};">{num}</div>
                <div class="stat-label">{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Disease cards ──
    st.markdown('<div class="section-header">🔬 Available Predictions</div>', unsafe_allow_html=True)
    d1, d2, d3 = st.columns(3)
    with d1:
        st.markdown("""
        <div class="info-card">
            <h4>🩺 Diabetes Prediction</h4>
            <p>Predicts diabetes risk using glucose, insulin, BMI, blood pressure & other metabolic indicators.</p>
            <br><span class="badge badge-blue">8 Features</span>
            <span class="badge badge-green" style="margin-left:6px;">97.9% Acc</span>
        </div>""", unsafe_allow_html=True)
    with d2:
        st.markdown("""
        <div class="info-card">
            <h4>❤️ Heart Disease</h4>
            <p>Assesses cardiovascular risk using cholesterol, ECG, blood pressure & exercise-angina data.</p>
            <br><span class="badge badge-blue">13 Features</span>
            <span class="badge badge-green" style="margin-left:6px;">100% Acc</span>
        </div>""", unsafe_allow_html=True)
    with d3:
        st.markdown("""
        <div class="info-card">
            <h4>🧠 Parkinson's Disease</h4>
            <p>Detects Parkinson's from voice signal biomarkers including jitter, shimmer & frequency variants.</p>
            <br><span class="badge badge-blue">13 Features</span>
            <span class="badge badge-purple" style="margin-left:6px;">100% Acc</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── How it works ──
    st.markdown('<div class="section-header">🔄 How It Works</div>', unsafe_allow_html=True)
    steps = st.columns(4)
    for col, (icon, title, desc) in zip(steps, [
        ("1️⃣", "Select Disease", "Choose from Diabetes, Heart Disease, or Parkinson's from the sidebar"),
        ("2️⃣", "Enter Parameters", "Fill in your clinical measurements and health indicators"),
        ("3️⃣", "Run Analysis", "Our Gradient Boosting model processes your data instantly"),
        ("4️⃣", "View Results", "Get a risk assessment with confidence score and color-coded output"),
    ]):
        with col:
            st.markdown(f"""
            <div class="info-card" style="text-align:center;">
                <div style="font-size:1.8rem;">{icon}</div>
                <h4 style="margin-top:8px;">{title}</h4>
                <p>{desc}</p>
            </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="disclaimer">
        ⚠️ <strong>Medical Disclaimer:</strong> MediScan AI is a research & educational tool only.
        Predictions are NOT a substitute for professional medical diagnosis.
        Always consult a licensed healthcare provider for medical decisions.
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PAGE — DIABETES
# ══════════════════════════════════════════════════════════════
elif page == "🩺  Diabetes Prediction":
    st.markdown('<h1 class="main-title">Diabetes Prediction</h1>', unsafe_allow_html=True)
    st.markdown('<p class="main-subtitle">Enter the patient\'s clinical parameters below</p>', unsafe_allow_html=True)

    with st.form("diabetes_form"):
        st.markdown('<div class="section-header">👤 Patient Demographics</div>', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1: pregnancies = st.number_input("Pregnancies", 0, 17, 1, help="Number of times pregnant")
        with col2: age         = st.number_input("Age (years)", 18, 81, 35)
        with col3: bmi         = st.number_input("BMI", 10.0, 70.0, 26.0, 0.1)
        with col4: dpf         = st.number_input("Diabetes Pedigree Function", 0.05, 2.50, 0.47, 0.001,
                                                  help="Family history likelihood score")

        st.markdown('<div class="section-header">🩸 Blood & Metabolic Indicators</div>', unsafe_allow_html=True)
        col5, col6, col7, col8 = st.columns(4)
        with col5: glucose         = st.number_input("Glucose (mg/dL)", 50, 200, 120, help="2-hr plasma glucose")
        with col6: insulin         = st.number_input("Insulin (μU/mL)", 0, 846, 80)
        with col7: blood_pressure  = st.number_input("Blood Pressure (mmHg)", 40, 122, 72)
        with col8: skin_thickness  = st.number_input("Skin Thickness (mm)", 0, 99, 20)

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🔍  Predict Diabetes Risk", use_container_width=True)

    if submitted:
        features = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
        pred, prob, _ = run_prediction("diabetes", features)
        col_r, col_s = st.columns([2, 1])
        with col_r:
            show_result(pred, prob,
                        "Diabetes Risk Detected", "No Diabetes Detected",
                        "⚠️", "✅",
                        "The model indicates elevated probability of diabetes.",
                        "The model indicates low probability of diabetes.")
        with col_s:
            st.markdown('<div class="info-card"><h4>📋 Input Summary</h4></div>', unsafe_allow_html=True)
            st.dataframe(pd.DataFrame({
                "Parameter": ["Pregnancies","Glucose","Blood Pressure","Skin Thickness","Insulin","BMI","DPF","Age"],
                "Value"    : features
            }), hide_index=True, use_container_width=True)

        st.markdown('<div class="disclaimer">⚠️ Consult an endocrinologist or physician for proper diagnosis.</div>',
                    unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PAGE — HEART DISEASE
# ══════════════════════════════════════════════════════════════
elif page == "❤️  Heart Disease":
    st.markdown('<h1 class="main-title">Heart Disease Prediction</h1>', unsafe_allow_html=True)
    st.markdown('<p class="main-subtitle">Enter cardiovascular clinical parameters for assessment</p>', unsafe_allow_html=True)

    with st.form("heart_form"):
        st.markdown('<div class="section-header">👤 Patient Information</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1: age  = st.number_input("Age", 25, 80, 52)
        with col2: sex  = st.selectbox("Sex", [("Male", 1), ("Female", 0)], format_func=lambda x: x[0])
        with col3: cp   = st.selectbox("Chest Pain Type",
                                        [(0,"Typical Angina"),(1,"Atypical Angina"),(2,"Non-anginal Pain"),(3,"Asymptomatic")],
                                        format_func=lambda x: x[1])

        st.markdown('<div class="section-header">💉 Vital Signs & Tests</div>', unsafe_allow_html=True)
        col4, col5, col6 = st.columns(3)
        with col4:
            trestbps = st.number_input("Resting BP (mmHg)", 90, 200, 130)
            chol     = st.number_input("Cholesterol (mg/dL)", 120, 600, 246)
        with col5:
            fbs     = st.selectbox("Fasting Blood Sugar > 120", [(0,"No"),(1,"Yes")], format_func=lambda x: x[1])
            restecg = st.selectbox("Resting ECG",
                                    [(0,"Normal"),(1,"ST-T Abnormality"),(2,"LV Hypertrophy")],
                                    format_func=lambda x: x[1])
        with col6:
            thalach = st.number_input("Max Heart Rate", 70, 202, 150)
            exang   = st.selectbox("Exercise Induced Angina", [(0,"No"),(1,"Yes")], format_func=lambda x: x[1])

        st.markdown('<div class="section-header">📈 Advanced Indicators</div>', unsafe_allow_html=True)
        col7, col8, col9, col10 = st.columns(4)
        with col7:  oldpeak = st.number_input("ST Depression", 0.0, 6.2, 1.0, 0.1)
        with col8:  slope   = st.selectbox("ST Slope", [(0,"Upsloping"),(1,"Flat"),(2,"Downsloping")], format_func=lambda x: x[1])
        with col9:  ca      = st.selectbox("Major Vessels", [0, 1, 2, 3, 4])
        with col10: thal    = st.selectbox("Thalassemia", [(0,"Normal"),(1,"Fixed Defect"),(2,"Reversible Defect"),(3,"Unknown")],
                                            format_func=lambda x: x[1])

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("❤️  Predict Heart Disease Risk", use_container_width=True)

    if submitted:
        features = [age, sex[1], cp[0], trestbps, chol, fbs[0], restecg[0], thalach, exang[0], oldpeak, slope[0], ca, thal[0]]
        pred, prob, _ = run_prediction("heart", features)
        show_result(pred, prob,
                    "Heart Disease Risk Detected", "No Heart Disease Detected",
                    "❗", "💚",
                    "The model indicates elevated cardiovascular risk.",
                    "The model indicates healthy cardiovascular indicators.")
        st.markdown('<div class="disclaimer">⚠️ Consult a cardiologist if you experience chest pain or shortness of breath.</div>',
                    unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PAGE — PARKINSON'S
# ══════════════════════════════════════════════════════════════
elif page == "🧠  Parkinson's Disease":
    st.markdown('<h1 class="main-title">Parkinson\'s Disease Prediction</h1>', unsafe_allow_html=True)
    st.markdown('<p class="main-subtitle">Voice signal biomarkers for Parkinson\'s risk assessment</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card" style="margin-bottom:20px;">
        <h4>ℹ️ About Voice-Based Detection</h4>
        <p>This model analyses vocal frequency, jitter, shimmer & noise ratios —
        biomarkers often altered in Parkinson's patients before other symptoms appear.</p>
    </div>""", unsafe_allow_html=True)

    with st.form("parkinsons_form"):
        st.markdown('<div class="section-header">🎵 Fundamental Frequency (Hz)</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1: fo  = st.number_input("MDVP: Fo — Average Vocal Freq", 80.0, 270.0, 154.228, 0.001)
        with col2: fhi = st.number_input("MDVP: Fhi — Max Vocal Freq",   100.0, 600.0, 197.105, 0.001)
        with col3: flo = st.number_input("MDVP: Flo — Min Vocal Freq",    65.0, 240.0, 116.082, 0.001)

        st.markdown('<div class="section-header">📊 Jitter & Shimmer Measures</div>', unsafe_allow_html=True)
        col4, col5, col6, col7 = st.columns(4)
        with col4: jitter  = st.number_input("MDVP Jitter (%)", 0.001, 0.030, 0.00662, 0.00001, format="%.5f")
        with col5: shimmer = st.number_input("Shimmer",          0.009, 0.300, 0.05416, 0.0001,  format="%.5f")
        with col6: nhr     = st.number_input("NHR",              0.001, 0.500, 0.01337, 0.0001,  format="%.5f")
        with col7: hnr     = st.number_input("HNR",              8.0,   35.0,  21.640,  0.001)

        st.markdown('<div class="section-header">🔢 Nonlinear Dynamical Measures</div>', unsafe_allow_html=True)
        col8, col9, col10, col11, col12, col13 = st.columns(6)
        with col8:  rpde    = st.number_input("RPDE",    0.20, 0.95, 0.414783, 0.0001, format="%.6f")
        with col9:  dfa     = st.number_input("DFA",     0.50, 0.97, 0.815285, 0.0001, format="%.6f")
        with col10: spread1 = st.number_input("Spread1", -9.0, -2.0, -4.813031, 0.0001, format="%.6f")
        with col11: spread2 = st.number_input("Spread2",  0.02, 0.55,  0.266482, 0.0001, format="%.6f")
        with col12: d2      = st.number_input("D2",       1.5,  4.0,   2.301442, 0.0001, format="%.6f")
        with col13: ppe     = st.number_input("PPE",      0.02, 0.70,  0.284654, 0.0001, format="%.6f")

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🧠  Predict Parkinson's Risk", use_container_width=True)

    if submitted:
        features = [fo, fhi, flo, jitter, shimmer, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]
        pred, prob, _ = run_prediction("parkinsons", features)
        show_result(pred, prob,
                    "Parkinson's Indicators Detected", "No Parkinson's Indicators",
                    "⚠️", "✅",
                    "Voice biomarkers suggest possible Parkinson's disease presence.",
                    "Voice biomarkers appear within normal ranges.")
        st.markdown('<div class="disclaimer">⚠️ Voice analysis is supplementary. Consult a neurologist for comprehensive evaluation.</div>',
                    unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PAGE — MODEL ANALYTICS
# ══════════════════════════════════════════════════════════════
elif page == "📊  Model Analytics":
    st.markdown('<h1 class="main-title">Model Analytics</h1>', unsafe_allow_html=True)
    st.markdown('<p class="main-subtitle">Performance metrics and dataset statistics</p>', unsafe_allow_html=True)

    diseases = {
        "🩺 Diabetes":         "diabetes",
        "❤️ Heart Disease":    "heart",
        "🧠 Parkinson's":      "parkinsons",
    }

    for label, key in diseases.items():
        try:
            _, _, metrics = load_model(key)
            train_df = pd.read_csv(DATASET_DIR / f"{key}_train.csv")
            test_df  = pd.read_csv(DATASET_DIR / f"{key}_test.csv")

            with st.expander(f"{label}  —  {metrics['accuracy']*100:.1f}% Accuracy", expanded=True):
                c1, c2, c3, c4 = st.columns(4)
                for col, (num, color, lbl) in zip([c1,c2,c3,c4], [
                    (f"{metrics['accuracy']*100:.1f}%", "#60a5fa", "Accuracy"),
                    (metrics['n_samples'],               "#a78bfa", "Total Samples"),
                    (metrics['n_train'],                 "#34d399", "Train Samples"),
                    (metrics['n_test'],                  "#fb923c", "Test Samples"),
                ]):
                    with col:
                        st.markdown(f"""
                        <div class="stat-card">
                            <div class="stat-number" style="color:{color};">{num}</div>
                            <div class="stat-label">{lbl}</div>
                        </div>""", unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                t1, t2 = st.tabs(["📋 Training Data Sample", "🧪 Test Data Sample"])
                with t1: st.dataframe(train_df.head(10), use_container_width=True, hide_index=True)
                with t2: st.dataframe(test_df.head(10),  use_container_width=True, hide_index=True)

                st.markdown(f'<div style="color:#6b7280;font-size:0.82rem;margin-top:8px;">Features: {", ".join(metrics["features"])}</div>',
                            unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Could not load {label}: {e}")


# ══════════════════════════════════════════════════════════════
# PAGE — ABOUT
# ══════════════════════════════════════════════════════════════
elif page == "ℹ️   About":
    st.markdown('<h1 class="main-title">About MediScan AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="main-subtitle">Technology, methodology, and acknowledgements</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>🤖 Machine Learning Model</h4>
            <p>MediScan AI uses <strong style="color:#60a5fa;">Gradient Boosting Classifiers</strong> —
            an ensemble method combining 200 decision trees for superior accuracy.
            Learning rate 0.1, max depth 5, trained with stratified 80/20 train-test split.</p>
        </div>
        <div class="info-card">
            <h4>📐 Feature Preprocessing</h4>
            <p>All inputs are normalised using <strong style="color:#60a5fa;">StandardScaler</strong>
            to ensure consistent scaling across parameters with different units (mg/dL, mmHg, Hz, etc.).</p>
        </div>
        <div class="info-card">
            <h4>📁 Data & Privacy</h4>
            <p>No patient data is stored or transmitted. All predictions occur locally in your session.
            Datasets are synthetically generated from known medical distributions for demonstration.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>🛠️ Tech Stack</h4>
            <p>
                <strong style="color:#60a5fa;">Frontend   :</strong> Streamlit<br>
                <strong style="color:#60a5fa;">ML Library :</strong> scikit-learn<br>
                <strong style="color:#60a5fa;">Data       :</strong> pandas, NumPy<br>
                <strong style="color:#60a5fa;">Storage    :</strong> joblib<br>
                <strong style="color:#60a5fa;">Language   :</strong> Python 3.8+
            </p>
        </div>
        <div class="info-card">
            <h4>⚕️ Medical Disclaimer</h4>
            <p>This application is for <strong style="color:#fbbf24;">educational & research purposes only</strong>.
            It is NOT a certified medical device and should never replace professional medical advice,
            diagnosis, or treatment.</p>
        </div>
        <div class="info-card">
            <h4>📬 Acknowledgements</h4>
            <p>Disease models inspired by the Pima Indians Diabetes Dataset, UCI Heart Disease Dataset,
            and the Oxford Parkinson's Disease Detection Dataset.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;padding:40px 0 20px;color:#4b5563;font-size:0.82rem;">
        MediScan AI — Built with ❤️ using Python & Streamlit<br>
        For educational purposes only • Not a medical device
    </div>""", unsafe_allow_html=True)
