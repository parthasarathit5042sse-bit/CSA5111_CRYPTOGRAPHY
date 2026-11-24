"""Module 1 - preprocessing and feature extraction."""
import re
import pandas as pd

URL_RE = re.compile(r"https?://[^\s]+", re.I)
SUSPICIOUS_WORDS = ["urgent", "verify", "password", "suspended", "immediately", "click", "login",
                    "bank", "otp", "credit card", "winner", "prize", "claim", "overdue", "expires",
                    "confirm", "locked", "final notice", "account"]
SUSPICIOUS_TLDS = (".xyz", ".top", ".ru", ".click", ".tk")

def clean_text(t: str) -> str:
    t = re.sub(r"http\S+", " URL ", str(t).lower())
    return re.sub(r"[^a-z0-9 ]+", " ", t)

def build_text(df: pd.DataFrame) -> pd.Series:
    return (df["subject"].fillna("") + " " + df["body"].fillna("")).map(clean_text)

def extract_indicators(sender: str, subject: str, body: str) -> dict:
    text = f"{subject} {body}".lower()
    urls = URL_RE.findall(f"{subject} {body}")
    sender_dom = sender.split("@")[-1].lower() if "@" in sender else ""
    return {
        "urls": urls,
        "keywords": [w for w in SUSPICIOUS_WORDS if w in text],
        "suspicious_sender": sender_dom.endswith(SUSPICIOUS_TLDS),
        "suspicious_urls": [u for u in urls if any(t in u.lower() for t in SUSPICIOUS_TLDS)],
        "sender_domain": sender_dom,
    }
