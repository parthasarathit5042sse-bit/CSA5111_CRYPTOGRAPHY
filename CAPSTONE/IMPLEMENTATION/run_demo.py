"""Console demo: trains the model, classifies sample emails and runs the PGP flow."""
import warnings; warnings.filterwarnings("ignore")
from model import train, load, predict
from features import extract_indicators
import pgp_utils as pgp

print("=" * 64, "\n MODULE 1+2: Training phishing classifier\n" + "=" * 64)
m = train()
print(f"Accuracy : {m['accuracy']:.4f}\nPrecision: {m['precision']:.4f}\nRecall   : {m['recall']:.4f}\nF1-score : {m['f1']:.4f}")
print("Confusion matrix [[TN, FP], [FN, TP]]:", m["confusion_matrix"])

samples = [
 ("paypal-support@secure-login.xyz", "URGENT: PayPal account suspended",
  "Dear customer, verify your password immediately at http://secure-login.xyz/login or your account will be closed."),
 ("kumar@university.edu", "Assignment submission reminder",
  "Dear students, the cryptography assignment is due next Monday. Submit it on the course portal."),
]
bundle = load()
print("\n" + "=" * 64, "\n MODULE 4: Detection + threat explanation\n" + "=" * 64)
for s, subj, body in samples:
    score, contrib = predict(subj, body, bundle)
    ind = extract_indicators(s, subj, body)
    print(f"\nFrom   : {s}\nSubject: {subj}")
    print(f"Result : {'PHISHING' if score >= 0.5 else 'LEGITIMATE'}  (phishing score = {score:.2f})")
    print("Top words :", ", ".join(f"{w} ({c:+.2f})" for w, c in contrib[:5]))
    print("Keywords  :", ind["keywords"], "| Suspicious sender:", ind["suspicious_sender"], "| Bad URLs:", ind["suspicious_urls"])
    if score >= 0.5: print("ALERT     : Do NOT click links or share credentials!")

print("\n" + "=" * 64, "\n MODULE 3: OpenPGP encryption & digital signature\n" + "=" * 64)
alice = pgp.generate_keypair("Alice", "alice@example.com")
bob = pgp.generate_keypair("Bob", "bob@example.com")
signed = pgp.sign_message("Hello Bob, project review is on Friday.", alice)
enc = pgp.encrypt_message(signed, bob.pubkey)
print("Encrypted message (first lines):\n" + "\n".join(str(enc).splitlines()[:4]) + "\n...")
dec = pgp.decrypt_message(enc, bob)
print("Decrypted text      :", dec.message)
print("Signature verified  :", pgp.verify_signature(dec, alice.pubkey))
tampered = pgp.sign_message("Original", alice); tampered._message = "Tampered"
print("Tampered signature  :", pgp.verify_signature(tampered, alice.pubkey))
