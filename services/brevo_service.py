import os
import requests
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")

BREVO_URL = "https://api.brevo.com/v3/smtp/email"


def send_email(enriched_person):

    recipient_email = enriched_person.get("email")

    if not recipient_email:
        print("No email found")
        return None

    first_name = enriched_person.get("first_name", "")
    full_name = enriched_person.get("full_name", "")
    company_name = enriched_person.get("company_name", "")
    company_website = enriched_person.get("company_website", "")
    linkedin_url = enriched_person.get("linkedin_url", "")

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <body>

        <p>Hi {first_name},</p>

        <p>
            I came across your profile while researching professionals at
            {company_name} and was impressed by your background.
        </p>

        <p>
            I'd love to connect and briefly discuss opportunities for collaboration.
        </p>

        <p>
            Company: {company_name}<br>
            Website: {company_website}<br>
            LinkedIn: {linkedin_url}
        </p>

        <p>
            Looking forward to hearing from you.
        </p>

        <p>
            Best Regards,<br>
            Raikant Chaudhary
        </p>

    </body>
    </html>
    """

    payload = {
        "sender": {
            "name": "Raikant Chaudhary",
            "email": "raikant@raikantchaudhary.tech"
        },
        "to": [
            {
                "email": recipient_email,
                "name": full_name
            }
        ],
        "subject": f"Connecting with {company_name}",
        "htmlContent": html_content
    }

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    response = requests.post(
        BREVO_URL,
        headers=headers,
        json=payload,
        timeout=60
    )

    print(response.status_code)
    print(response.text)

    return response.json()

if __name__ == "__main__":

    test_person = {
        "first_name": "Sahil",
        "last_name": "Chaudhary",
        "full_name": "Sahil Chaudhary",

        # Your own email for testing
        "email": "sahilsahil102060@gmail.com",

        "linkedin_url": "https://www.linkedin.com/in/test",

        "company_name": "Google",
        "company_website": "https://google.com",
        "company_linkedin_url": "https://www.linkedin.com/company/google"
    }

    result = send_email(test_person)

    print("\n========== BREVO RESPONSE ==========")

    print(result)