# Minimal CPU image
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./
ENV PROVIDER=huggingface HF_MODEL_NAME=google/flan-t5-base
EXPOSE 8501

CMD ["bash", "-lc", "streamlit run ListingBoost/app/app.py --server.port 8501 --server.address 0.0.0.0"]
