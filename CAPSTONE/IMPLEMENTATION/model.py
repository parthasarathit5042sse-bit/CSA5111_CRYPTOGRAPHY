"""Module 2 - ML classification (TF-IDF + Logistic Regression)  and
Module 4 - explanation (top contributing words from model coefficients)."""
import joblib, pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from features import build_text, clean_text

MODEL_PATH = "model.joblib"

def train(csv="data/emails.csv"):
    df = pd.read_csv(csv)
    X, y = build_text(df), df["label"]
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    vec = TfidfVectorizer(ngram_range=(1, 2), min_df=2, stop_words="english")
    clf = LogisticRegression(max_iter=1000)
    clf.fit(vec.fit_transform(Xtr), ytr)
    pred = clf.predict(vec.transform(Xte))
    metrics = {"accuracy": accuracy_score(yte, pred), "precision": precision_score(yte, pred),
               "recall": recall_score(yte, pred), "f1": f1_score(yte, pred),
               "confusion_matrix": confusion_matrix(yte, pred).tolist()}
    joblib.dump({"vec": vec, "clf": clf, "metrics": metrics}, MODEL_PATH)
    return metrics

def load():
    try:
        return joblib.load(MODEL_PATH)
    except FileNotFoundError:
        train(); return joblib.load(MODEL_PATH)

def predict(subject, body, bundle=None):
    bundle = bundle or load()
    vec, clf = bundle["vec"], bundle["clf"]
    text = clean_text(f"{subject} {body}")
    x = vec.transform([text])
    score = float(clf.predict_proba(x)[0][1])
    # Explainability: contribution = tf-idf value * coefficient
    names = vec.get_feature_names_out()
    coo = x.tocoo()
    contrib = sorted(((names[j], float(v * clf.coef_[0][j])) for j, v in zip(coo.col, coo.data)),
                     key=lambda t: -abs(t[1]))[:8]
    return score, contrib
