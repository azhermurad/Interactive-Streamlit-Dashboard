# 🐧 Palmer's Penguins Dataset Overview

Palmer's Penguins dataset, providing a more comprehensive view of penguin characteristics and their environment. It includes new features such as diet, year of observation, life stage, and health metrics, in addition to the original attributes. The dataset spans from 2021 to 2025.

---

### 📋 Columns Description

| Column | Description |
|--------|-------------|
| **Species** | Species of the penguin (*Adelie, Chinstrap, Gentoo*) |
| **Island** | Island where the penguin was found (*Biscoe, Dream, Torgensen*) |
| **Sex** | Gender of the penguin (*Male, Female*) |
| **Diet** | Primary diet of the penguin (*Fish, Krill, Squid*) |
| **Year** | Year the data was collected (*2021–2025*) |
| **Life Stage** | Life stage of the penguin (*Chick, Juvenile, Adult*) |
| **Body Mass (g)** | Body mass in grams |
| **Bill Length (mm)** | Bill length in millimeters |
| **Bill Depth (mm)** | Bill depth in millimeters |
| **Flipper Length (mm)** | Flipper length in millimeters |
| **Health Metrics** | Health status (*Healthy, Overweight, Underweight*) |

---

# Streamlit Setup Guide

Follow these steps to set up and run a Streamlit application in a virtual environment.

---

## 0. Clone Repo

```bash
git clone git@github.com:azhermurad/Interactive-Streamlit-Dashboard.git
```

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
