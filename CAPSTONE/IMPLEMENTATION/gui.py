"""PhishGuard AI - Tkinter desktop GUI for the capstone demo.
Run from this folder: python gui.py
"""
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

BASE = Path(__file__).resolve().parent
import sys
sys.path.insert(0, str(BASE))
from features import extract_indicators
from model import load, train, predict

BG = "#0b1220"
PANEL = "#111c30"
ACCENT = "#38bdf8"
TEXT = "#e5edf7"
MUTED = "#94a3b8"

class App:
    def __init__(self, root):
        self.root = root
        root.title("PhishGuard AI | Email Security")
        root.geometry("1120x760")
        root.minsize(950, 680)
        root.configure(bg=BG)
        self.setup_style()
        self.bundle = None
        self.build()
        self.load_model()

    def setup_style(self):
        s = ttk.Style()
        try: s.theme_use("clam")
        except tk.TclError: pass
        s.configure("TFrame", background=BG)
        s.configure("Panel.TFrame", background=PANEL)
        s.configure("TLabel", background=BG, foreground=TEXT, font=("Segoe UI", 10))
        s.configure("Panel.TLabel", background=PANEL, foreground=TEXT, font=("Segoe UI", 10))
        s.configure("Muted.TLabel", background=PANEL, foreground=MUTED)
        s.configure("Title.TLabel", background=BG, foreground=TEXT, font=("Segoe UI", 24, "bold"))
        s.configure("Sub.TLabel", background=BG, foreground=MUTED, font=("Segoe UI", 10))
        s.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), padding=10)
        s.configure("TNotebook", background=BG, borderwidth=0)
        s.configure("TNotebook.Tab", padding=(16, 10), font=("Segoe UI", 10, "bold"))

    def build(self):
        header = ttk.Frame(self.root, padding=(24, 18)); header.pack(fill="x")
        ttk.Label(header, text="🛡  PHISHGUARD AI", style="Title.TLabel").pack(anchor="w")
        ttk.Label(header, text="AI-assisted phishing detection • Secure communication • Explainable alerts", style="Sub.TLabel").pack(anchor="w", pady=(5,0))
        self.status = tk.Label(header, text="MODEL: LOADING", bg="#172554", fg="#bfdbfe", padx=12, pady=5, font=("Segoe UI", 9, "bold"))
        self.status.pack(anchor="e", pady=(0,4))

        nb = ttk.Notebook(self.root); nb.pack(fill="both", expand=True, padx=22, pady=(0,20))
        self.analysis_tab = ttk.Frame(nb); self.security_tab = ttk.Frame(nb); self.metrics_tab = ttk.Frame(nb)
        nb.add(self.analysis_tab, text="  Email Analyzer  "); nb.add(self.security_tab, text="  OpenPGP Security  "); nb.add(self.metrics_tab, text="  Model Metrics  ")
        self.build_analysis(); self.build_security(); self.build_metrics()

    def panel(self, parent, title):
        f = ttk.Frame(parent, style="Panel.TFrame", padding=16)
        ttk.Label(f, text=title, style="Panel.TLabel", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0,10))
        return f

    def build_analysis(self):
        tab=self.analysis_tab
        left=ttk.Frame(tab, style="Panel.TFrame", padding=16); left.pack(side="left", fill="both", expand=True, padx=(12,6), pady=12)
        right=ttk.Frame(tab, style="Panel.TFrame", padding=16); right.pack(side="left", fill="both", expand=True, padx=(6,12), pady=12)
        ttk.Label(left,text="EMAIL DETAILS",style="Panel.TLabel",font=("Segoe UI",12,"bold")).pack(anchor="w",pady=(0,12))
        self.sender=self.entry(left,"Sender email", "example@domain.com")
        self.subject=self.entry(left,"Subject", "")
        ttk.Label(left,text="Message body",style="Panel.TLabel").pack(anchor="w",pady=(10,5))
        self.body=tk.Text(left,height=13,wrap="word",bg="#0a1020",fg=TEXT,insertbackground=TEXT,relief="flat",font=("Segoe UI",10),padx=10,pady=10)
        self.body.pack(fill="both",expand=True)
        btn=tk.Button(left,text="  ANALYZE EMAIL  ",command=self.analyze,bg="#0284c7",fg="white",activebackground="#0369a1",relief="flat",font=("Segoe UI",11,"bold"),padx=14,pady=10);btn.pack(fill="x",pady=(14,0))
        ttk.Label(right,text="ANALYSIS & EXPLANATION",style="Panel.TLabel",font=("Segoe UI",12,"bold")).pack(anchor="w")
        self.result=tk.Label(right,text="Paste an email and click Analyze.\n\nThis is a decision-support demo; verify suspicious messages independently.",bg=PANEL,fg=MUTED,justify="left",wraplength=450,font=("Segoe UI",11),anchor="nw");self.result.pack(fill="x",pady=12)
        self.score=tk.Label(right,text="Risk score: —",bg="#172554",fg="#bfdbfe",font=("Segoe UI",14,"bold"),padx=12,pady=10);self.score.pack(fill="x",pady=(0,12))
        ttk.Label(right,text="Detected indicators",style="Panel.TLabel",font=("Segoe UI",10,"bold")).pack(anchor="w")
        self.indicators=tk.Text(right,height=13,wrap="word",bg="#0a1020",fg=TEXT,relief="flat",font=("Segoe UI",10),padx=10,pady=10);self.indicators.pack(fill="both",expand=True,pady=(6,0));self.indicators.configure(state="disabled")

    def entry(self,parent,label,placeholder):
        ttk.Label(parent,text=label,style="Panel.TLabel").pack(anchor="w",pady=(8,4))
        e=tk.Entry(parent,bg="#0a1020",fg=TEXT,insertbackground=TEXT,relief="flat",font=("Segoe UI",10));e.pack(fill="x",ipady=8)
        if placeholder: e.insert(0,placeholder)
        return e

    def build_security(self):
        f=ttk.Frame(self.security_tab,style="Panel.TFrame",padding=24);f.pack(fill="both",expand=True,padx=12,pady=12)
        ttk.Label(f,text="OPENPGP — SENDER AUTHENTICATION & EMAIL SECURITY",style="Panel.TFrame",font=("Segoe UI",14,"bold")).pack(anchor="w",pady=(0,14))
        text=("Module 3 of the capstone demonstrates OpenPGP-based secure communication.\n\n"
              "• Public/private key pairs support secure message exchange.\n• Encryption helps protect message confidentiality.\n"
              "• Digital signatures help verify message integrity and signer authenticity.\n• Decryption is performed by the authorized private-key holder.\n\n"
              "This GUI tab describes the security workflow. It does not perform cryptographic operations here; use GnuPG/OpenPGP separately for an actual encryption or signature test.")
        tk.Label(f,text=text,bg=PANEL,fg=TEXT,justify="left",wraplength=850,font=("Segoe UI",12),anchor="nw").pack(fill="both",expand=True)

    def build_metrics(self):
        f=ttk.Frame(self.metrics_tab,style="Panel.TFrame",padding=24);f.pack(fill="both",expand=True,padx=12,pady=12)
        ttk.Label(f,text="MODEL EVALUATION",style="Panel.TFrame",font=("Segoe UI",14,"bold")).pack(anchor="w",pady=(0,14))
        self.metrics_text=tk.Label(f,text="Model metrics will appear here after training/loading.",bg=PANEL,fg=TEXT,justify="left",font=("Segoe UI",12));self.metrics_text.pack(anchor="w",pady=10)
        tk.Button(f,text="Train / Refresh model",command=self.refresh_model,bg="#334155",fg="white",relief="flat",padx=12,pady=9).pack(anchor="w",pady=10)
        ttk.Label(f,text="Metrics are calculated from the dataset's held-out test split. Synthetic data results are illustrative only.",style="Muted.TLabel",wraplength=800).pack(anchor="w",pady=10)

    def load_model(self):
        try:
            self.bundle=load()
            self.status.config(text="MODEL: READY",bg="#14532d",fg="#bbf7d0")
            self.show_metrics(self.bundle.get("metrics",{}))
        except Exception as e:
            self.status.config(text="MODEL: ERROR",bg="#7f1d1d",fg="#fecaca")
            messagebox.showerror("Model load error",str(e))

    def refresh_model(self):
        try:
            metrics=train(str(BASE/"data"/"emails.csv"));self.bundle=load()
            self.show_metrics(metrics);messagebox.showinfo("Training complete","Model trained and saved.")
        except Exception as e: messagebox.showerror("Training error",str(e))

    def show_metrics(self,m):
        if not m:return
        labels=[("Accuracy",m.get("accuracy")),("Precision",m.get("precision")),("Recall",m.get("recall")),("F1-score",m.get("f1"))]
        self.metrics_text.config(text="\n\n".join(f"{k}: {v:.1%}" for k,v in labels if v is not None)+f"\n\nConfusion matrix: {m.get('confusion_matrix','N/A')}")

    def analyze(self):
        sender=self.sender.get().strip();subject=self.subject.get().strip();body=self.body.get("1.0","end").strip()
        if not subject and not body:messagebox.showwarning("Missing email","Enter a subject or body to analyze.");return
        try:
            score,contrib=predict(subject,body,self.bundle)
            flags=extract_indicators(sender,subject,body)
            label="LIKELY PHISHING" if score>=0.5 else "LIKELY LEGITIMATE"
            self.result.config(text=label,fg="#fca5a5" if score>=.5 else "#86efac")
            self.score.config(text=f"Model phishing score: {score:.1%}",bg="#7f1d1d" if score>=.5 else "#14532d",fg="#fee2e2" if score>=.5 else "#dcfce7")
            lines=[f"Sender domain: {flags['sender_domain'] or 'not detected'}",f"URLs found: {len(flags['urls'])}",f"Suspicious keywords: {', '.join(flags['keywords']) or 'none detected'}",f"Suspicious URL indicators: {', '.join(flags['suspicious_urls']) or 'none detected'}",f"Sender-domain flag: {'yes' if flags['suspicious_sender'] else 'no'}","","Model influential terms:"]
            lines += [f"  {term}: {weight:+.4f}" for term,weight in contrib] or ["  No terms returned"]
            lines += ["","Reminder: this is a model prediction, not a guarantee."]
            self.indicators.configure(state="normal");self.indicators.delete("1.0","end");self.indicators.insert("end","\n".join(lines));self.indicators.configure(state="disabled")
        except Exception as e:messagebox.showerror("Analysis error",str(e))

if __name__=="__main__":
    root=tk.Tk();App(root);root.mainloop()
