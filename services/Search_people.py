import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

PROSPEO_API_KEY = os.getenv("PROSPEO_API_KEY")
URL = "https://api.prospeo.io/search-person?filters=true&page=1"


def search_people_by_domain(domain, page=1):
    headers = {
        "X-KEY": PROSPEO_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "filters": {
            "person_search": {
                "include": [domain],
                "match_mode": "SMART"
            }
        },
        "page": page
    }

    try:
        response = requests.post(
            URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        print(f"\nSTATUS CODE: {response.status_code}")

        response.raise_for_status()

        data = response.json()

        people = []

        for result in data.get("results", []):

            person = result.get("person", {})
            company = result.get("company", {})

            company_name = company.get("name")
            company_website = company.get("website")
            company_linkedin_url = company.get("linkedin_url")

            people.append({
                "person_id": person.get("person_id"),

                "first_name": person.get("first_name"),
                "last_name": person.get("last_name"),

                "full_name": person.get("full_name"),

                "linkedin_url": person.get("linkedin_url"),

                "email": (
                    person.get("email", {})
                    .get("email")
                    if isinstance(person.get("email"), dict)
                    else None
                ),

                "company_name": company_name,
                "company_website": company_website,
                "company_linkedin_url": company_linkedin_url
            })

        return people

    except Exception as e:
        print(f"\nERROR: {e}")
        return []
