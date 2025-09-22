import argparse, pathlib
from ListingBoost.app.utils import ListingContext, load_prompt_template, render_prompt, CaptionGenerator

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--bhk", required=True)
    p.add_argument("--area", required=True)
    p.add_argument("--locality", required=True)
    p.add_argument("--city", required=True)
    p.add_argument("--price", required=True)
    p.add_argument("--amenities", required=True)
    p.add_argument("--tone", default="luxury")
    p.add_argument("--highlights", default="")
    args = p.parse_args()

    ctx = ListingContext(**vars(args))
    tmpl_path = pathlib.Path(__file__).resolve().parents[1] / "prompts" / "base_prompt.txt"
    tmpl = load_prompt_template(str(tmpl_path))
    prompt = render_prompt(tmpl, ctx)

    gen = CaptionGenerator()
    text = gen.generate(prompt)
    print("\n=== Generated Caption ===\n")
    print(text)

if __name__ == "__main__":
    main()
