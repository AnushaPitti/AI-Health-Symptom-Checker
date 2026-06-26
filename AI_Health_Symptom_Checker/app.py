"""
app.py
------
Flask web application for the AI Health Symptom Checker.

Features:
    * User registration and login (SQLite + hashed passwords)
    * Symptom input via checkboxes (with voice input support)
    * ML-based disease prediction with confidence score
    * Data visualizations (Matplotlib + Seaborn)
    * Downloadable PDF health report
    * Rule-based chatbot health assistant
    * Light / Dark mode toggle
"""

import os
import sqlite3
from flask import (Flask, render_template, request, redirect, url_for,
                   session, flash, send_file, jsonify)
from werkzeug.security import generate_password_hash, check_password_hash

from symptom_checker import (predict_disease, get_ai_suggestion,
                             SYMPTOM_COLUMNS)
from report_generator import generate_text_report, generate_pdf_report
from visualizations import generate_all_charts

# ------------------------------------------------------------------
# Flask Configuration
# ------------------------------------------------------------------
app = Flask(__name__)
app.config["SECRET_KEY"] = "ai_health_symptom_checker_secret_key_2026"

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "users.db")


# ------------------------------------------------------------------
# Database Helpers
# ------------------------------------------------------------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email    TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


init_db()


def db_query(query, args=(), one=False, commit=False):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    if commit:
        conn.commit()
        conn.close()
        return None
    rows = cur.fetchall()
    conn.close()
    return (rows[0] if rows else None) if one else rows


# ------------------------------------------------------------------
# Authentication Decorator
# ------------------------------------------------------------------
from functools import wraps

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "username" not in session:
            flash("Please log in to continue.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper


# ------------------------------------------------------------------
# Routes
# ------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not username or not email or not password:
            flash("All fields are required.", "danger")
            return redirect(url_for("register"))

        hashed = generate_password_hash(password)
        try:
            db_query("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                     (username, email, hashed), commit=True)
            flash("Registration successful. Please log in.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Username or email already exists.", "danger")
            return redirect(url_for("register"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = db_query("SELECT * FROM users WHERE username = ?",
                        (username,), one=True)
        if user and check_password_hash(user["password"], password):
            session["username"] = user["username"]
            flash(f"Welcome back, {user['username']}!", "success")
            return redirect(url_for("dashboard"))
        flash("Invalid credentials. Please try again.", "danger")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("index"))


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    # Pre-generate charts so they are always available
    generate_all_charts()
    return render_template("dashboard.html",
                           symptoms=SYMPTOM_COLUMNS,
                           username=session["username"])


@app.route("/predict", methods=["POST"])
@login_required
def predict():
    selected = request.form.getlist("symptoms")
    symptom_dict = {col: (1 if col in selected else 0) for col in SYMPTOM_COLUMNS}

    disease, confidence = predict_disease(symptom_dict)
    suggestion = get_ai_suggestion(disease)

    # Generate text + PDF reports
    generate_text_report(session["username"], selected, disease, confidence, suggestion)
    generate_pdf_report(session["username"], selected, disease, confidence, suggestion)

    # Generate charts
    generate_all_charts()

    return render_template("result.html",
                           username=session["username"],
                           symptoms=selected,
                           disease=disease,
                           confidence=confidence,
                           suggestion=suggestion)


@app.route("/download_report")
@login_required
def download_report():
    path = os.path.join(BASE_DIR, "reports", f"health_report_{session['username']}.pdf")
    if not os.path.exists(path):
        flash("No report available. Please run a prediction first.", "warning")
        return redirect(url_for("dashboard"))
    return send_file(path, as_attachment=True)


# ------------------------------------------------------------------
# Rule-based Chatbot
# ------------------------------------------------------------------
CHATBOT_RULES = {
    "hello": "Hi there! I'm your AI Health Assistant. How can I help you today?",
    "hi": "Hello! How are you feeling today?",
    "fever": "Stay hydrated, rest, and take paracetamol if needed. See a doctor if it persists more than 3 days.",
    "cough": "Try warm fluids and steam inhalation. Persistent cough should be evaluated by a doctor.",
    "headache": "Rest in a quiet room, hydrate, and avoid screens. Persistent headaches need medical attention.",
    "covid": "If you suspect COVID-19, isolate immediately and take a test. Monitor oxygen levels.",
    "thanks": "You're welcome! Take care and stay healthy.",
    "bye": "Goodbye! Wishing you good health.",
}


@app.route("/chatbot", methods=["GET", "POST"])
@login_required
def chatbot():
    if request.method == "POST":
        msg = request.json.get("message", "").lower().strip()
        reply = "I'm sorry, I didn't understand that. Could you describe your symptoms?"
        for key, value in CHATBOT_RULES.items():
            if key in msg:
                reply = value
                break
        return jsonify({"reply": reply})
    return render_template("chatbot.html")


# ------------------------------------------------------------------
# Run
# ------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
