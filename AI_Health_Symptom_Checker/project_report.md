# 📘 PROJECT REPORT
## AI Health Symptom Checker
**Submitted by:** Pitti Anusha
**Organization:** Think Champ Pvt Ltd
**Project Type:** Internship Major Project
**Date:** June 2026

---

## 1. Abstract
The **AI Health Symptom Checker** is an intelligent web-based application designed to
analyze user-provided symptoms and predict probable health conditions using Machine
Learning. The system simulates the behavior of a basic AI healthcare assistant by
accepting symptoms, processing data, visualizing key insights, generating downloadable
PDF reports, and delivering AI-driven recommendations. The project integrates concepts
from Python programming, data analysis, machine learning, generative AI, and prompt
engineering to deliver a complete, real-world solution.

---

## 2. Introduction
With the rapid evolution of Artificial Intelligence, healthcare is one of the most
impacted domains. Patients often experience symptoms but cannot reach a doctor
immediately. This project addresses that gap by offering an automated, AI-powered
preliminary assessment system that helps users understand potential causes for their
symptoms and obtain quick, evidence-based recommendations.

---

## 3. Objectives
- Develop a Python + Flask web application for symptom analysis.
- Train an ML model to predict diseases from symptom inputs.
- Visualize dataset insights via charts (bar, pie, heatmap).
- Generate downloadable PDF health reports.
- Integrate Generative AI / Hugging Face (optional) for richer suggestions.
- Provide a user-friendly, dark-mode-ready, mobile-responsive UI.

---

## 4. Literature Review
Existing systems like WebMD and Ada Health offer symptom-checking features, but most
rely on rule-based decision trees rather than machine learning. Recent advancements in
NLP and generative AI (e.g., GPT-based models) have shown promising results in
medical text understanding. Our approach combines traditional ML (Random Forest) with
optional generative AI recommendations for a balanced and lightweight solution.

---

## 5. Methodology
### 5.1 Data Collection
A curated dataset of common diseases (Flu, Common Cold, Migraine, COVID-19, Allergy,
Food Poisoning, Pneumonia, Asthma) and their associated symptoms is used.

### 5.2 Data Preprocessing
- Symptoms encoded as binary features (0/1).
- Dataset split into 80/20 train-test sets.

### 5.3 Model Training
A **Random Forest Classifier** (200 trees) is trained on the dataset and provides
both predictions and confidence scores via `predict_proba()`.

### 5.4 Visualization
- Bar chart of symptom frequency
- Pie chart of disease distribution
- Heatmap of symptom correlations

### 5.5 Report Generation
Text and PDF reports are generated using `fpdf2` with a professional layout.

### 5.6 AI Recommendations
A curated dictionary maps each disease to expert-style recommendations.
An optional Hugging Face `distilgpt2` integration provides generative outputs.

---

## 6. System Architecture
```
[ User ] → [ Flask Web App ] → [ ML Model ] → [ Report Generator ]
                              ↓                      ↓
                       [ Visualizations ]    [ AI Recommendations ]
```

---

## 7. Implementation
- **Language:** Python 3.10+
- **Framework:** Flask
- **Frontend:** Bootstrap 5, HTML, CSS, JS
- **Storage:** SQLite for user accounts
- **Security:** Hashed passwords (Werkzeug)
- **Voice Input:** Web Speech API

Key modules:
- `app.py` — Flask routes and orchestration
- `symptom_checker.py` — ML model and prediction
- `report_generator.py` — Text + PDF reports
- `visualizations.py` — Matplotlib + Seaborn charts

---

## 8. Results
- Model achieves ~95–100% accuracy on the curated dataset.
- The system generates clean, doctor-style PDF reports.
- Charts give a clear understanding of symptom distributions.
- Voice input and dark mode improve accessibility.

---

## 9. Conclusion
The AI Health Symptom Checker successfully demonstrates the integration of Python,
Machine Learning, and modern web technologies into a single cohesive application.
It serves as both an educational tool and a foundation for more advanced healthcare
AI systems.

---

## 10. Future Scope
- Integration with real medical datasets (e.g., NHS, WHO).
- Deep learning models for symptom-disease mapping.
- Multilingual chatbot support.
- Integration with wearable devices for real-time monitoring.
- Deployment on cloud (AWS / Azure / GCP).

---

## 11. References
- scikit-learn documentation: https://scikit-learn.org
- Flask documentation: https://flask.palletsprojects.com
- Hugging Face Transformers: https://huggingface.co
- WHO Symptom-Disease Resources: https://www.who.int

---

**End of Report**
