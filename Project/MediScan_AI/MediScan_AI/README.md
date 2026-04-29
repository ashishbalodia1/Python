# 🏥 MediScan AI — Disease Prediction System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.32-red?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/scikit--learn-1.4-orange?logo=scikitlearn" alt="sklearn">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

> **AI-powered disease risk prediction** for Diabetes, Heart Disease, and Parkinson's Disease using Gradient Boosting Machine Learning models — wrapped in a clean, dark-themed Streamlit web app.

---

## 📸 Screenshots

| Home Page | Prediction Result |
|-----------|------------------|
| Dark medical dashboard | Color-coded risk cards |

---

## 🧠 Diseases Covered

| Disease | Features | Model | Accuracy |
|---------|----------|-------|----------|
| 🩺 **Diabetes** | Glucose, BMI, Insulin, Blood Pressure, etc. | GBM | ~97.9% |
| ❤️ **Heart Disease** | Cholesterol, ECG, Thalach, Angina, etc. | GBM | ~100% |
| 🧠 **Parkinson's** | Voice MDVP Fo/Fhi/Flo, Jitter, Shimmer, etc. | GBM | ~100% |

---

## 📁 Project Structure

```
MediScan_AI/
│
├── app.py                          # ← Main Streamlit application
├── requirements.txt                # ← Python dependencies
├── runtime.txt                     # ← Python version for deployment
├── .gitignore                      # ← Git ignore rules
├── README.md                       # ← This file
│
├── dataset/                        # ← Train / Test / Full CSVs
│   ├── diabetes_train.csv
│   ├── diabetes_test.csv
│   ├── diabetes_full.csv
│   ├── heart_train.csv
│   ├── heart_test.csv
│   ├── heart_full.csv
│   ├── parkinsons_train.csv
│   ├── parkinsons_test.csv
│   └── parkinsons_full.csv
│
├── saved_models/                   # ← Trained model & scaler .pkl files
│   ├── diabetes_model.pkl
│   ├── diabetes_scaler.pkl
│   ├── diabetes_metrics.json
│   ├── heart_model.pkl
│   ├── heart_scaler.pkl
│   ├── heart_metrics.json
│   ├── parkinsons_model.pkl
│   ├── parkinsons_scaler.pkl
│   └── parkinsons_metrics.json
│
└── colab_files_to_train_models/    # ← Google Colab training notebook
    └── MediScan_AI_Train_Models.ipynb
```

---

## 🚀 Quick Start (Local)

### 1. Clone the repository
```bash
git clone https://github.com/ashishbalodia1/MediScan_AI.git
cd MediScan_AI
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## ☁️ Deploy on Streamlit Cloud (Free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"** → Connect your GitHub repo
4. Set **Main file path** → `app.py`
5. Click **Deploy** 🎉

---

## 🔬 Model Details

### Algorithm: Gradient Boosting Classifier
```
n_estimators  = 200
max_depth     = 5
learning_rate = 0.1
random_state  = 42
```

### Preprocessing
- **StandardScaler** applied to all features before training and inference
- **Stratified train/test split** (80% train, 20% test)

### Re-training Models (optional)
Open the Colab notebook in `colab_files_to_train_models/` and run all cells.
Download the generated `.pkl` and `.json` files into `saved_models/`
and the `.csv` files into `dataset/`.

---

## 📊 Feature Reference

### 🩺 Diabetes (8 features)
| Feature | Description |
|---------|-------------|
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose level (mg/dL) |
| BloodPressure | Diastolic blood pressure (mmHg) |
| SkinThickness | Triceps skinfold thickness (mm) |
| Insulin | 2-Hour serum insulin (μU/mL) |
| BMI | Body Mass Index (kg/m²) |
| DiabetesPedigreeFunction | Family history likelihood score |
| Age | Age in years |

### ❤️ Heart Disease (13 features)
| Feature | Description |
|---------|-------------|
| age | Patient age |
| sex | Sex (1=Male, 0=Female) |
| cp | Chest pain type (0–3) |
| trestbps | Resting blood pressure (mmHg) |
| chol | Serum cholesterol (mg/dL) |
| fbs | Fasting blood sugar > 120 mg/dL |
| restecg | Resting ECG results |
| thalach | Max heart rate achieved |
| exang | Exercise-induced angina |
| oldpeak | ST depression induced by exercise |
| slope | Slope of peak exercise ST segment |
| ca | Number of major vessels (0–4) |
| thal | Thalassemia type |

### 🧠 Parkinson's Disease (13 features)
| Feature | Description |
|---------|-------------|
| MDVP_Fo_Hz | Average vocal fundamental frequency |
| MDVP_Fhi_Hz | Maximum vocal frequency |
| MDVP_Flo_Hz | Minimum vocal frequency |
| MDVP_Jitter_pct | Vocal jitter percentage |
| Shimmer | Amplitude shimmer |
| NHR | Noise-to-Harmonics Ratio |
| HNR | Harmonics-to-Noise Ratio |
| RPDE | Recurrence Period Density Entropy |
| DFA | Detrended Fluctuation Analysis |
| spread1, spread2 | Nonlinear fundamental freq variation |
| D2 | Correlation dimension |
| PPE | Pitch Period Entropy |

---

## ⚠️ Medical Disclaimer

> **This application is for educational and research purposes ONLY.**
> It is NOT a certified medical device and must NOT be used as a substitute
> for professional medical advice, diagnosis, or treatment.
> Always consult a qualified healthcare professional for medical decisions.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) — UCI ML Repository
- [Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease) — UCI ML Repository
- [Parkinson's Disease Dataset](https://archive.ics.uci.edu/ml/datasets/parkinsons) — Oxford / UCI ML Repository
- [Streamlit](https://streamlit.io/) — Web framework
- [scikit-learn](https://scikit-learn.org/) — ML library

---

<p align="center">Made with ❤️ using Python & Streamlit</p>

---

## Author

Ashish Balodia — https://github.com/ashishbalodia1

