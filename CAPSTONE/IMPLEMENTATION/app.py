"""Module 4 - Streamlit dashboard: detection, explanation, alerts and PGP tools."""
import warnings; warnings.filterwarnings("ignore")
import streamlit as st, plotly.express as px, pandas as pd
from model import load, predict, train
from features import extract_indicators
import pgp_utils as pgp

st.set_page_config(page_title="AI Phishing Detection & Secure Email", page_icon="🛡️", layout="wide")
st.title("🛡️ AI-Assisted Phishing Email Detection and Secure Communication")
bundle = load()
tab1, tab2, tab3 = st.tabs(["📧 Phishing Detection", "🔐 PGP Secure Email", "📊 Model Performance"])

with tab1:
    c1, c2 = st.columns(2)
    sender = c1.text_input("Sender", "paypal-support@secure-login.xyz")
    subject = c1.text_input("Subject", "URGENT: PayPal account suspended")
    body = c1.text_area("Body", "Dear customer, verify your password immediately at http://secure-login.xyz/login or your account will be closed.", height=150)
    if c1.button("Analyze Email", type="primary"):
        score, contrib = predict(subject, body, bundle)
        ind = extract_indicators(sender, subject, body)
        with c2:
            if score >= 0.5: st.error(f"🚨 PHISHING DETECTED — score {score:.2%}")
            else: st.success(f"✅ LEGITIMATE — phishing score {score:.2%}")
            st.progress(score)
            st.write("**Suspicious keywords:**", ", ".join(ind["keywords"]) or "none")
            st.write("**Sender domain:**", ind["sender_domain"], "⚠️ suspicious" if ind["suspicious_sender"] else "")
            st.write("**URLs:**", ", ".join(ind["urls"]) or "none")
            if score >= 0.5: st.warning("ALERT: Do not click links or share credentials.")
            df = pd.DataFrame(contrib, columns=["word", "contribution"])
            st.plotly_chart(px.bar(df, x="contribution", y="word", orientation="h",
                                   title="Why this prediction? (top feature contributions)"), use_container_width=True)

with tab2:
    st.write("Generate keys, then sign + encrypt a message (Alice → Bob) and verify on the receiving side.")
    msg = st.text_area("Message", "Hello Bob, the project review is on Friday.")
    if st.button("Run secure communication demo"):
        alice, bob = pgp.generate_keypair("Alice", "alice@example.com"), pgp.generate_keypair("Bob", "bob@example.com")
        enc = pgp.encrypt_message(pgp.sign_message(msg, alice), bob.pubkey)
        st.code(str(enc), language="text")
        dec = pgp.decrypt_message(enc, bob)
        st.write("**Decrypted:**", dec.message)
        if pgp.verify_signature(dec, alice.pubkey):
            st.success("Signature VERIFIED ✔")
        else:
            st.error("Signature INVALID ✘")

with tab3:
    if st.button("Retrain model"): train(); st.cache_data.clear(); bundle = load()
    m = bundle["metrics"]
    cols = st.columns(4)
    for col, k in zip(cols, ["accuracy", "precision", "recall", "f1"]): col.metric(k.title(), f"{m[k]:.3f}")
    cm = pd.DataFrame(m["confusion_matrix"], index=["Actual Legit", "Actual Phish"], columns=["Pred Legit", "Pred Phish"])
    st.plotly_chart(px.imshow(cm, text_auto=True, title="Confusion Matrix"), use_container_width=True)
