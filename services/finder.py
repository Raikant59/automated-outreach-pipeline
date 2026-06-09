import json
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

FINDER_API_KEY = os.getenv("FINDER_API_KEY")

genai.configure(api_key=FINDER_API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")



def get_similar_company_domains(domain):
    prompt = f"""
        You are a company intelligence expert.

        Find all companies similar to the company with domain:
        {domain}

        IMPORTANT RULES:
        1. Return ONLY REAL and EXISTING companies.
        2. NEVER invent, guess, create, or hallucinate company names or domains.
        3. Every domain must belong to a company that actually exists.
        4. If you are not confident that a company exists, DO NOT include it.
        5. Exclude duplicates.
        6. Exclude the input company itself.
        7. Return as many real similar companies as you can find.
        8. Return ONLY JSON.
        9. No markdown.
        10. No explanations.
        11. No confidence scores.

        Output format:

        {{
        "domains": [
            "company1.com",
            "company2.com",
            "company3.com"
        ]
        }}

        If you cannot confidently identify a company as real, leave it out.
        """

    response = model.generate_content(prompt)

    try:
        text = response.text.strip()

        text = text.replace("```json", "").replace("```", "").strip()

        data = json.loads(text)

        all_domains = data.get("domains", [])

        return set(all_domains)

    except Exception as e:
        print(f"Similar company error: {e}")
        return set()

