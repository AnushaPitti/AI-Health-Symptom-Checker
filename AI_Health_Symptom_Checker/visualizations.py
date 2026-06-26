"""
visualizations.py
------------------
Generates data visualizations using Matplotlib and Seaborn.
All charts are saved into /static/charts/ for use by the web app.
"""

import os
import matplotlib
matplotlib.use("Agg")  # Non-GUI backend (required for Flask)
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

CHARTS_DIR = os.path.join(os.path.dirname(__file__), "static", "charts")
os.makedirs(CHARTS_DIR, exist_ok=True)

DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset.csv")


def _load():
    return pd.read_csv(DATASET_PATH)


def symptom_frequency_chart():
    """Bar chart - frequency of each symptom across dataset."""
    df = _load()
    symptom_cols = df.columns[:-1]
    freq = df[symptom_cols].sum().sort_values(ascending=False)

    plt.figure(figsize=(9, 5))
    sns.barplot(x=freq.values, y=freq.index, palette="viridis")
    plt.title("Symptom Frequency in Dataset", fontsize=14, fontweight="bold")
    plt.xlabel("Number of Occurrences")
    plt.ylabel("Symptom")
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, "symptom_frequency.png")
    plt.savefig(path, dpi=120)
    plt.close()
    return path


def disease_distribution_chart():
    """Pie chart - distribution of diseases in dataset."""
    df = _load()
    counts = df["Disease"].value_counts()

    plt.figure(figsize=(7, 7))
    plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%",
            startangle=140, colors=sns.color_palette("Set2"))
    plt.title("Disease Distribution", fontsize=14, fontweight="bold")
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, "disease_distribution.png")
    plt.savefig(path, dpi=120)
    plt.close()
    return path


def symptom_correlation_heatmap():
    """Heatmap - correlation between symptoms."""
    df = _load()
    symptom_cols = df.columns[:-1]
    corr = df[symptom_cols].corr()

    plt.figure(figsize=(9, 7))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Symptom Correlation Heatmap", fontsize=14, fontweight="bold")
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, "symptom_correlation.png")
    plt.savefig(path, dpi=120)
    plt.close()
    return path


def generate_all_charts():
    """Generate and return the paths of all visualizations."""
    return {
        "frequency": symptom_frequency_chart(),
        "distribution": disease_distribution_chart(),
        "correlation": symptom_correlation_heatmap(),
    }
