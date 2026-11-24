# AI-Assisted Phishing Email Detection and Secure Communication Framework
Windows / Python 3.9+:
1. `pip install -r requirements.txt`
2. `python generate_dataset.py`   (creates sample data/emails.csv; use your own CSV with columns sender,subject,body,label)
3. `python run_demo.py`           (console output of all 4 modules)
4. `streamlit run app.py`         (web dashboard)   -- or just double-click run.bat
Files: features.py (Module 1), model.py (Module 2 + explanation), pgp_utils.py (Module 3), app.py (Module 4 dashboard)
