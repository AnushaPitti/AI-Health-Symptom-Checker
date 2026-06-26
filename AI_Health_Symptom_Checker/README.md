# 🩺 AI Health Symptom Checker

An AI-powered web application that analyzes user-reported symptoms and predicts
possible health conditions using Machine Learning. Built as the **Internship Major Project**
at **Think Champ Pvt Ltd**.

---

## 📌 Project Overview
The **AI Health Symptom Checker** is a Python + Flask based intelligent application
that:
- Accepts symptoms from users via web UI or voice
- Predicts the most likely disease using a trained ML model
- Generates rich data visualizations
- Produces downloadable PDF health reports
- Provides AI-driven recommendations
- Includes a rule-based health chatbot

---

## 🚀 Features
✅ User Registration & Login (SQLite + hashed passwords)
✅ Symptom Input (Checkboxes + Voice Input via Web Speech API)
✅ Disease Prediction with Confidence Score (Random Forest Classifier)
✅ Data Visualizations using Matplotlib & Seaborn
✅ AI-Generated Health Suggestions
✅ Optional Hugging Face Generative AI integration
✅ Professional PDF Health Report Generation
✅ Rule-Based Health Chatbot
✅ Light / Dark Mode Toggle
✅ Mobile-Responsive Bootstrap 5 UI

---

## 🧠 Tech Stack
| Category        | Tools                                    |
| --------------- | ---------------------------------------- |
| Language        | Python 3.10+                             |
| Web Framework   | Flask                                    |
| ML              | scikit-learn (RandomForestClassifier)    |
| Data Analysis   | NumPy, Pandas                            |
| Visualization   | Matplotlib, Seaborn                      |
| PDF Reports     | fpdf2                                    |
| Frontend        | HTML5, CSS3, Bootstrap 5, JavaScript     |
| Generative AI   | Hugging Face Transformers (Optional)     |
| Database        | SQLite                                   |

---

## 📁 Folder Structure
```
AI_Health_Symptom_Checker/
│
├── app.py                  # Main Flask application
├── symptom_checker.py      # ML model + prediction logic
├── report_generator.py     # Text & PDF report generation
├── visualizations.py       # Matplotlib + Seaborn charts
├── dataset.csv             # Symptom-Disease dataset
├── requirements.txt
├── README.md
├── project_report.md       # Detailed project report
│
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── result.html
│   └── chatbot.html
│
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   └── charts/             # Generated charts
│
└── reports/                # Generated health reports
```

---

## ⚙️ Installation & Setup

1. **Clone or extract** the project folder.
2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux / Mac
   venv\Scripts\activate       # Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```bash
   python app.py
   ```
5. Open your browser at: **http://127.0.0.1:5000**

---

## 🧪 Usage
1. Register a new account.
2. Login with your credentials.
3. Select your symptoms (or use 🎤 voice input).
4. Click **Analyze Symptoms** → view your prediction.
5. Download your **PDF Health Report**.
6. Use the **Chatbot** for quick health Q&A.

---

## 📸 Screenshots

### 🏠 Home Page (Light Mode)
https://github.com/AnushaPitti/AI-Health-Symptom-Checker/blob/main/screenshots/welcome%20message.jpeg

### 🌙 Home Page (Dark Mode)
https://github.com/AnushaPitti/AI-Health-Symptom-Checker/blob/main/screenshots/welcome%20page%20with%20user%20name.jpeg

### 📝 Registration Page
https://github.com/AnushaPitti/AI-Health-Symptom-Checker/blob/main/screenshots/Registration%20page.jpeg

### 👋 Dashboard - Welcome
<img src="screenshots/welcome page with user name.jpeg" width="100%"/>

### 🩺 Symptom Selection
https://github.com/AnushaPitti/AI-Health-Symptom-Checker/blob/main/screenshots/symptom%20input.jpeg

### 🔍 Disease Prediction
https://github.com/AnushaPitti/AI-Health-Symptom-Checker/blob/main/screenshots/disease%20prediction.jpeg

### 💬 AI Chatbot
https://github.com/AnushaPitti/AI-Health-Symptom-Checker/blob/main/screenshots/AI%20chatbot%20for%20symptoms%20input.jpeg

### 📊 Data Visualizations
https://github.com/AnushaPitti/AI-Health-Symptom-Checker/blob/main/screenshots/data%20analysis%20and%20visulization.jpeg

### 🖥️ Terminal Output
https://github.com/AnushaPitti/AI-Health-Symptom-Checker/blob/main/screenshots/cmd%20output.png
``
---

## 👩‍💻 Author
**Pitti Anusha**
Associate Instrumentation Engineer | Intern @ Think Champ Pvt Ltd

---

## ⚠️ Disclaimer
This application is intended for **educational purposes only**.
Always consult a qualified medical professional for health advice.

---

## 📄 License
MIT License © 2026 Pitti Anusha
