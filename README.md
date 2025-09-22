

## 1. Problem Statement
Real estate agents at **Sahai Estates** were spending **30–45 minutes** writing marketing captions for each property listing.
- Slow, repetitive, and inconsistent process.
- Delays in posting = missed engagement opportunities.
- Lack of consistency in tone and style across platforms.

## 2. Business Need
- Faster content creation for high-end property listings.
- Consistency in language and tone across portals, WhatsApp, and social media.
- Higher engagement & inquiries leading to faster deal closures.

## 3. Solution (Technical Approach)
Built a **GPT-powered automation tool** with Hugging Face + Streamlit:

- Prompt Engineering → Added property-specific context (location, size, amenities, price).
- Fine-tuned GPT on property descriptions & luxury real estate marketing style.
- User Interface → Simple Streamlit app for agents to generate captions instantly.
- Deployment → Python backend, Hugging Face Transformers, AWS S3 for hosting.

**Tech Stack:** `Python | Hugging Face (Transformers, PEFT, TRL) | Streamlit | AWS S3`

## 4. Results (Impact)
- 70% reduction in time (30 min → <5 min per caption).
- 2x higher engagement rate (measured via inquiries).
- 20+ hours/month saved for the sales team.

## 5. Sample Output
**Input:** `3BHK, 1800 sq ft, Sea-facing, Worli, ₹12 Cr, 2 Car Parks, Clubhouse Access`

**Generated Caption:**  
\"Wake up to breathtaking sea views every morning. This 3BHK luxury apartment in Worli offers 1800 sq ft of elegant living with modern amenities, 2 car parks, and exclusive clubhouse access. A rare gem priced at ₹12 Cr. Book your private tour today!\"

## 6. Transferability
The framework is **domain-agnostic** and can be extended:
- E-commerce → Product description automation.
- Travel → Personalized itinerary captions.
- Marketing → Social media ad copy generation.

## Case Study Slide Template

### Slide 1 – Challenge
- Agents spent 30–45 mins writing each caption.
- Inconsistent tone across listings.
- Lost time = fewer deals closed.

### Slide 2 – Solution
- GPT-powered caption generator.
- Prompt engineering with property context (location, amenities, price).
- Streamlit app for easy use.

### Slide 3 – Results
- Caption time reduced by 70%.
- Engagement rate on listings doubled.
- Sales team saved 20+ hours/month.

### Slide 4 – Scalability
- Can be applied to e-commerce, travel, or marketing domains.
- Reusable framework for AI-driven content automation.
"""
