"""Builds a labelled sample email dataset (data/emails.csv).
Replace data/emails.csv with a real dataset (columns: sender, subject, body, label)
to train on real data. label: 1 = phishing, 0 = legitimate."""
import random, pandas as pd
random.seed(42)

brands = ["PayPal", "Amazon", "Microsoft", "Netflix", "HDFC Bank", "SBI", "Apple", "Google"]
bad_dom = ["secure-login.xyz", "verify-account.top", "account-alert.ru", "update-info.click", "support-desk.tk"]
good_dom = ["university.edu", "company.com", "gmail.com", "outlook.com", "college.ac.in"]
phish_t = [
 ("URGENT: {b} account suspended", "Dear customer, your {b} account has been suspended. Verify your password immediately at http://{d}/login or your account will be closed within 24 hours."),
 ("Security alert - confirm your identity", "We detected unusual activity. Click here http://{d}/verify to confirm your bank details and OTP now to avoid permanent suspension."),
 ("You have won a prize!", "Congratulations! You are selected for a reward. Claim your gift card now, send your credit card number and password at http://{d}/claim."),
 ("Payment failed - update billing", "Your {b} payment failed. Update your billing information immediately: http://{d}/billing. Failure to act will lock your account."),
 ("Invoice overdue - action required", "Final notice! Your invoice is overdue. Open the attachment and login to verify your account urgently http://{d}/invoice."),
 ("Password expires today", "Your password expires today. Click the link http://{d}/reset and enter your username and password to keep access."),
]
legit_t = [
 ("Meeting notes - project review", "Hi team, please find the notes from today's project review. Next meeting is on Friday at 10 AM in the seminar hall. Regards, {n}"),
 ("Assignment submission reminder", "Dear students, the cryptography assignment is due next Monday. Submit it on the course portal. Let me know if you have doubts. - {n}"),
 ("Lunch tomorrow?", "Hey, are you free for lunch tomorrow? We can try the new cafe near campus. Let me know. Thanks, {n}"),
 ("Your order has shipped", "Hello, your order #{o} has shipped and will arrive in 3 days. You can track it from your account page. Thank you for shopping with us."),
 ("Weekly newsletter", "Here is this week's newsletter with department news, seminar schedules and upcoming events. Have a great week! {n}"),
 ("Project report feedback", "I reviewed your draft report. The methodology section is good, please add more details to the results chapter and resubmit by Thursday. {n}"),
]
names = ["Priya", "Rahul", "Dr. Kumar", "Anita", "Suresh", "Meena"]

rows = []
for _ in range(600):
    s, b = random.choice(phish_t); br, d = random.choice(brands), random.choice(bad_dom)
    rows.append((f"{br.lower().replace(' ','')}-support@{d}", s.format(b=br), b.format(b=br, d=d), 1))
for _ in range(600):
    s, b = random.choice(legit_t)
    rows.append((f"{random.choice(names).split()[-1].lower()}@{random.choice(good_dom)}", s,
                 b.format(n=random.choice(names), o=random.randint(10000, 99999)), 0))
random.shuffle(rows)
pd.DataFrame(rows, columns=["sender", "subject", "body", "label"]).to_csv("data/emails.csv", index=False)
print("Saved data/emails.csv with", len(rows), "emails")
