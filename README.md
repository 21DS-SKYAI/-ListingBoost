# ListingBoost — GPT-Powered Real Estate Caption Generator

**Goal:** Generate persuasive, on-brand listing captions in seconds.

This repo contains a minimal, production-ready demo (Streamlit app + CLI) that you can run locally
or deploy (Docker). It uses **Hugging Face Transformers** by default (offline-capable) and can be
swapped to **OpenAI** or other providers via a simple strategy pattern.

---

## 🔧 Features
- Streamlit UI for brokers/marketers
- Prompt template with property context (location, BHK, area, price, amenities, tone)
- Local **Hugging Face** pipeline (default: `google/flan-t5-base` for text2text) — replace with any model you prefer
- Optional **OpenAI** backend (set `PROVIDER=openai` + `OPENAI_API_KEY` in `.env`)
- Reusable Python module (`listingboost/`) for programmatic use
- Sample data + a quick notebook
- Dockerfile and GitHub Actions CI stub

---

## 🏁 Quickstart

### 1) Setup
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

### 2) Run Streamlit app
```bash
streamlit run ListingBoost/app/app.py
```

### 3) CLI usage
```bash
python ListingBoost/inference/generate_caption.py \  --bhk 3 --area 1800 --locality Worli --city Mumbai \  --price "₹12 Cr" --amenities "2 Car Parks, Clubhouse" --tone "luxury"
```

---

## 🔀 Switch model/provider
Set in `.env`:
```
PROVIDER=huggingface     # or: openai
HF_MODEL_NAME=google/flan-t5-base
OPENAI_MODEL=gpt-4o-mini
OPENAI_API_KEY=sk-...
```

> Tip: For **better marketing copy**, try an instruction-tuned LLM. For **private/offline**, use a local HF model.
Replace `google/flan-t5-base` with a stronger model (e.g., `google/flan-t5-large`) if you have GPU/RAM.

---

## 📦 Project Structure
```
ListingBoost/
  app/
    app.py
    utils.py
  prompts/
    base_prompt.txt
  inference/
    generate_caption.py
  data/
    sample_listings.csv
  notebooks/
    listingboost_quickstart.ipynb
requirements.txt
.env.example
Dockerfile
.github/workflows/ci.yml
```

---

## 🧪 Example prompt → output
**Input context:** 3BHK, 1800 sq ft, Sea-facing, Worli, ₹12 Cr, 2 Car Parks, Clubhouse  
**Output (sample):** *"Wake up to sweeping sea views in this elegant 3BHK at Worli. 1800 sq ft of refined living with 2 car parks and exclusive clubhouse access. Priced at ₹12 Cr. Book your private tour."*

---

## 📈 Notes
- The demo uses a lightweight HF model so it runs on CPU. For production, integrate a stronger hosted model.
- You can log generations and A/B test tones in your marketing stack.
- Pair this with a RAG layer to include society/tower highlights automatically.

---

## 🛡️ Safety & Compliance
- Never paste secrets into code. Use `.env`.
- Review generated content for accuracy and compliance (RERA, fair-housing, etc.).

---

## 📝 License
MIT
