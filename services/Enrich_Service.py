import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

PROSPEO_API_KEY = os.getenv("PROSPEO_API_KEY")

ENRICH_URL = "https://api.prospeo.io/enrich-person"


def enrich_person(person_data):

    headers = {
        "X-KEY": PROSPEO_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "only_verified_email": True,
        "data": {
            "person_id": person_data["person_id"]
        }
    }

    try:
        response = requests.post(
            ENRICH_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        data = response.json()

        if data.get("error"):
            return {
                "success": False,
                "error": data.get("error_code")
            }

        person = data.get("person", {})
        company = data.get("company", {})

        return {
            "success": True,

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

            "email_status": (
                person.get("email", {})
                .get("status")
                if isinstance(person.get("email"), dict)
                else None
            ),

            "mobile": (
                person.get("mobile", {})
                .get("mobile")
                if isinstance(person.get("mobile"), dict)
                else None
            ),

            "company_name": company.get("name"),
            "company_website": company.get("website"),
            "company_linkedin_url": company.get("linkedin_url")
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
