<img width="1451" height="828" alt="image" src="https://github.com/user-attachments/assets/be03165f-ef2b-43c4-aac7-a1926daf653f" /># Financial Impulse Detection System - VR Sona (22MIA1161)

An AI-powered behavioral analytics platform that detects impulsive financial patterns using machine learning and behavioral signal engineering.

---

## Objective

The objective of this project is to:

- Detect impulsive spending patterns using ML
- Analyze behavioral financial signals
- Provide explainable AI insights
- Generate strategic financial recommendations
- Present results through an interactive modern dashboard

This system combines behavioral psychology + anomaly detection + volatility modeling to classify financial behavior into meaningful categories.

---

## What This System Does

The platform:

✔ Calculates Impulse Risk Score (0–100%)  
✔ Detects financial behavior type  
✔ Classifies severity (Low / Medium / High)  
✔ Calculates confidence score  
✔ Generates AI-written executive summary  
✔ Provides ML explainability breakdown  
✔ Produces strategic recommendations  

---

## Machine Learning Engine

The backend uses:

- Isolation Forest (Anomaly Detection)
- Volatility Scoring
- Behavioral Signal Engineering:
  - Night Spending Ratio
  - Weekend Ratio
  - End-of-Month Ratio
  - Spending Frequency
- Weighted Risk Aggregation Model

---

## Architecture
Frontend (Next.js + Tailwind + Recharts)
↓
FastAPI Backend
↓
ML Scoring Engine
↓
Behavioral Classification

---


---

## Project Structure
financial-impulse-detection/
│
├── api/ # FastAPI backend
│ ├── app.py
│ ├── engine.py
│ ├── scoring.py
│ ├── profiles.py
│ ├── nudges.py
│ ├── finance.db
│ └── requirements.txt
│
├── impulse-frontend/ # Next.js frontend
│ ├── app/
│ ├── components/
│ ├── globals.css
│ └── package.json
│
├── data/
│ └── synthetic_transactions.csv
│
├── models/
├── notebooks/
├── README.md
└── requirements.txt

---


---

## Features Implemented

### Risk Detection
- Impulse Risk Score (percentage)
- Behavioral Severity Classification
- Confidence Score

### Interactive Dashboard
- Risk Gauge
- Spending Trend Chart
- Category Distribution Pie Chart
- Radar Behavior Chart
- Feature Cards

### AI Insights
- Executive Summary
- Behavior Detection Banner (Dynamic Color)
- ML Explainability Breakdown
- Professional Strategic Recommendations

---

### Dashboard Overview

<img width="1469" height="576" alt="image" src="https://github.com/user-attachments/assets/e5d99649-68e8-401f-be9a-9d5d17f1af79" />

<img width="1450" height="831" alt="image" src="https://github.com/user-attachments/assets/725fc3a7-6fc3-4846-b402-b041b17c2071" />

---

### Risk Gauge + Feature Cards

<img width="1451" height="828" alt="image" src="https://github.com/user-attachments/assets/0d98d99f-5f05-49f7-a4a4-54166cd35b22" />

<img width="708" height="371" alt="image" src="https://github.com/user-attachments/assets/076f9647-2eda-42ec-9c17-3050b117edd1" />

<img width="700" height="445" alt="image" src="https://github.com/user-attachments/assets/9aac0b4f-463c-46eb-a257-510781faca83" />

<img width="1414" height="460" alt="image" src="https://github.com/user-attachments/assets/cb044268-1e4a-4ea7-91ca-2905f3458926" />

---

### Behaviour Analysis & Recommendations

<img width="1451" height="812" alt="image" src="https://github.com/user-attachments/assets/81d1f5ef-2f9c-4584-839a-9c4a55b294f6" />


---

### ML Explainability Breakdown

<img width="784" height="376" alt="image" src="https://github.com/user-attachments/assets/66c75f29-0ee8-4ae4-b8f5-c327e82bf795" />

---

## Deployment

### Frontend
- Built using **Next.js**
- Can be deployed on:
  - Vercel
  - Netlify

### Backend
- Built using **FastAPI**
- Can be deployed on:
  - Render
  - Railway
  - AWS EC2
  - DigitalOcean

---

## Local Setup Instructions

### Backend Setup
cd api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload

---

### Frontend Setup
cd impulse-frontend
npm install
npm run dev





