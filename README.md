<h1 align="center">ListingBoost 🏡 — AI Marketing Analytics for Real Estate Listings</h1>

<p align="center">
<img src="docs/brand_banner.png" alt="ListingBoost banner" width="800"/>
</p>

**Tagline:** Optimize listing performance across portals & social media using data-driven recommendations (captions, CTA, timing, price tweaks).

---

## 🚀 Project Summary
**ListingBoost** is an end-to-end system that ingests listing performance data (portals + social), analyzes trends, scores listings, and recommends marketing actions (caption templates, best posting times, CTA suggestions) to improve engagement and conversion rates.

**Outcome:** Increased listing leads and engagement; designed for real estate agents and small brokerages.

---

## 🔎 Problem
Real estate agents post many listings across portals and social media but lack consistent analytics to measure which listings perform and why. Manual optimization is time-consuming and inconsistent.

---

## 💡 Solution (What ListingBoost Does)
- Ingests listing metadata + portal analytics + social engagement
- Feature engineering for listing attributes (images, description length, price, location)
- Builds ranking & uplift models to predict listing engagement
- Generates actionable marketing suggestions:
  - Caption templates (GPT-powered)
  - Best posting time (hour/day recommendations)
  - Call-to-action (CTA) optimization
  - Price sensitivity flags
- Provides an interactive demo (Streamlit) and exportable report

---

## ⭐ Features
- Data ingestion & cleaning pipeline
- Exploratory analysis notebooks
- ML models for engagement / uplift
- Caption generation with prompt templates
- Streamlit demo dashboard with filters and recommendations
- CI tests & reproducible environment

---

## 📁 Repo Structure
(See repo root)  
Key directories: `src/`, `notebooks/`, `demo/`, `data/`, `docs/`.

---

## 📈 Demo
Run the demo locally (Streamlit):

```bash
pip install -r requirements.txt
streamlit run demo/streamlit_app.py
