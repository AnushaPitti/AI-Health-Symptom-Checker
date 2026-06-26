"""
symptom_checker.py
-------------------
Core Machine Learning module of the AI Health Symptom Checker.
Trains a Random Forest classifier on the symptom dataset and
provides a function to predict the most probable disease along
with a confidence score.

Author : Pitti Anusha
"""

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset.csv")

# Ordered list of symptom features (must match dataset columns)
SYMPTOM_COLUMNS = [
    "Fever", "Cough", "Headache", "Fatigue", "SoreThroat",
    "RunnyNose", "BodyAche", "Nausea", "Shortness_of_Breath", "Chest_Pain"
]


def load_dataset(path: str = DATASET_PATH) -> pd.DataFrame:
    """Load the health symptom dataset from CSV."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at: {path}")
    return pd.read_csv(path)


def train_model():
    """Train a Random Forest classifier on the dataset."""
    df = load_dataset()
    X = df[SYMPTOM_COLUMNS]
    y = df["Disease"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"[INFO] Model trained successfully. Test accuracy: {accuracy*100:.2f}%")
    return model


# Train once at import time (small dataset, fast)
MODEL = train_model()


def predict_disease(symptoms: dict):
    """
    Predict possible disease from a dictionary of symptoms.

    Parameters
    ----------
    symptoms : dict
        Dictionary like {"Fever": 1, "Cough": 1, ...}

    Returns
    -------
    tuple : (predicted_disease, confidence_score)
    """
    try:
        features = np.array([[symptoms.get(col, 0) for col in SYMPTOM_COLUMNS]])
        probabilities = MODEL.predict_proba(features)[0]
        classes = MODEL.classes_
        idx = int(np.argmax(probabilities))
        disease = classes[idx]
        confidence = round(float(probabilities[idx]) * 100, 2)
        return disease, confidence
    except Exception as e:
        print(f"[ERROR] Prediction failed: {e}")
        return "Unknown", 0.0


# AI-based health recommendations (Prompt-engineered baseline)
AI_SUGGESTIONS = {
    "Flu": "Drink plenty of fluids, take adequate rest, and use paracetamol for fever. Consult a doctor if symptoms last more than 5 days.",
    "Common Cold": "Stay hydrated, get rest, and try steam inhalation. Use a saline nasal spray to relieve congestion.",
    "Migraine": "Rest in a quiet, dark room. Avoid screens, stay hydrated, and consider over-the-counter pain relievers.",
    "COVID-19": "Isolate immediately, monitor oxygen levels, hydrate, and consult a healthcare provider. Get a confirmatory RT-PCR test.",
    "Allergy": "Avoid known allergens, use antihistamines, and keep your environment dust-free.",
    "Food Poisoning": "Drink ORS, stay hydrated, eat light food (bananas, rice, toast). Seek medical care if vomiting persists.",
    "Pneumonia": "Seek medical attention promptly. Antibiotics may be required. Rest and stay hydrated.",
    "Asthma": "Use prescribed inhalers, avoid triggers (dust, smoke), and consult a pulmonologist if breathing worsens.",
    "Unknown": "Please consult a qualified medical professional for an accurate diagnosis."
}


def get_ai_suggestion(disease: str) -> str:
    """Return AI-generated health suggestion for the predicted disease."""
    return AI_SUGGESTIONS.get(disease, AI_SUGGESTIONS["Unknown"])


# -----------------------------------------------------------
# Optional: Hugging Face Generative AI Integration
# -----------------------------------------------------------
def get_generative_suggestion(disease: str, symptoms: list) -> str:
    """
    (Optional) Use a Hugging Face model to generate a richer suggestion.
    Falls back gracefully if transformers / torch are not installed.
    """
    try:
        from transformers import pipeline
        generator = pipeline("text-generation", model="distilgpt2")
        prompt = (
            f"A patient reports the following symptoms: {', '.join(symptoms)}. "
            f"They are likely suffering from {disease}. "
            f"Provide a short, professional health recommendation:"
        )
        result = generator(prompt, max_length=80, num_return_sequences=1, do_sample=True)
        return result[0]["generated_text"]
    except Exception:
        return get_ai_suggestion(disease)
