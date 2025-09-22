import streamlit as st
from ListingBoost.app.utils import ListingContext, load_prompt_template, render_prompt, CaptionGenerator
import os, pathlib

st.set_page_config(page_title="ListingBoost — Caption Generator", layout="centered")

st.title("🏡 ListingBoost — GPT-Powered Captions")
st.caption("Generate persuasive, on-brand property captions in seconds.")

col1, col2 = st.columns(2)
with col1:
    bhk = st.text_input("Configuration (BHK)", "3")
    area = st.text_input("Area (sq ft)", "1800")
    locality = st.text_input("Locality", "Worli")
    city = st.text_input("City", "Mumbai")

with col2:
    price = st.text_input("Price", "₹12 Cr")
    amenities = st.text_input("Amenities", "2 Car Parks, Clubhouse")
    tone = st.selectbox("Tone", ["luxury", "professional", "warm", "minimal", "emoji-light"], index=0)
    highlights = st.text_input("Highlights (optional)", "Sea-facing, high floor")

if st.button("Generate Caption", type="primary"):
    ctx = ListingContext(
        bhk=bhk, area=area, locality=locality, city=city,
        price=price, amenities=amenities, tone=tone, highlights=highlights
    )
    tmpl_path = pathlib.Path(__file__).resolve().parents[1] / "prompts" / "base_prompt.txt"
    tmpl = load_prompt_template(str(tmpl_path))
    prompt = render_prompt(tmpl, ctx)

    gen = CaptionGenerator()
    with st.spinner("Crafting your caption..."):
        text = gen.generate(prompt)

    st.subheader("✨ Caption")
    st.write(text)

    st.download_button("Download .txt", text, file_name="caption.txt")

with st.expander("🔍 Debug — Prompt Preview"):
    st.code("Rendered Prompt:\n\n" + (locals().get("prompt") or ""), language="markdown")
