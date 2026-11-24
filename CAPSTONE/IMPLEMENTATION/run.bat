@echo off
pip install -r requirements.txt
python generate_dataset.py
python run_demo.py
streamlit run app.py
