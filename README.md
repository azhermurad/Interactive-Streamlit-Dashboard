# Streamlit Setup Guide

Follow these steps to set up and run a Streamlit application in a virtual environment.

---

## 1. Create a Virtual Environment

```bash
python -m venv .venv
```

---

## 2. Activate the Virtual Environment

### Windows (Command Prompt)
```bash
.venv\Scripts\activate.bat
```

### macOS and Linux
```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

Make sure you have a `requirements.txt` file. Then run:

```bash
pip install -r requirements.txt
```

---

## 4. Run the Streamlit App

```bash
streamlit run app.py
```

**OR**

```bash
python -m streamlit run app.py
```

---

## 📚 Full Documentation

Find the complete Streamlit documentation here:  
[Streamlit Installation Guide](https://docs.streamlit.io/get-started/installation/command-line)
