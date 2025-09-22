import os
from dataclasses import dataclass
from typing import Optional, Dict
from dotenv import load_dotenv

load_dotenv()

@dataclass
class ListingContext:
    bhk: str
    area: str
    locality: str
    city: str
    price: str
    amenities: str
    tone: str = os.getenv("DEFAULT_TONE", "luxury")
    highlights: str = ""

def load_prompt_template(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def render_prompt(tmpl: str, ctx: ListingContext) -> str:
    return tmpl.format(
        bhk=ctx.bhk,
        area=ctx.area,
        locality=ctx.locality,
        city=ctx.city,
        price=ctx.price,
        amenities=ctx.amenities,
        tone=ctx.tone,
        highlights=ctx.highlights or "—",
    )

class CaptionGenerator:
    def __init__(self):
        self.provider = os.getenv("PROVIDER", "huggingface").lower()
        if self.provider == "openai":
            from openai import OpenAI
            self.client = OpenAI()
            self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        else:
            from transformers import pipeline
            self.hf_model = os.getenv("HF_MODEL_NAME", "google/flan-t5-base")
            task = "text2text-generation"  # works for T5/FLAN family
            self.pipe = pipeline(task, model=self.hf_model)

    def generate(self, prompt: str) -> str:
        temperature = float(os.getenv("TEMPERATURE", "0.7"))
        max_tokens = int(os.getenv("MAX_TOKENS", "256"))
        if self.provider == "openai":
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role":"system","content":"You are a concise real-estate copywriter."},
                          {"role":"user","content":prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return resp.choices[0].message.content.strip()
        else:
            out = self.pipe(prompt, max_length=max_tokens, do_sample=True, temperature=temperature)
            text = out[0]["generated_text"]
            return text.strip()
