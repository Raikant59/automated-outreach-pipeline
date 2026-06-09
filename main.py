from services.finder import get_similar_company_domains
from services.Search_people import search_people_by_domain
from services.Enrich_Service import enrich_person
from services.brevo_service import send_email


def main():

    processed_persons = set()
    processed_emails = set()

    domain = input("Enter company domain: ").strip()

    print("\nFinding similar companies....\n")

    domains = get_similar_company_domains(domain)

    if not domains:
        print("No similar domains found\n")
        return

    print(f"Found {len(domains)} domains")

    total_sent = 0
    total_skipped = 0

    for company_domain in domains:

        print("\n" + "=" * 70)
        print(f"Processing: {company_domain}")
        print("=" * 70)

        try:

            people = search_people_by_domain(
                company_domain
            )

            if not people:
                print("No people found")
                continue

            for person in people:
                person_id = person.get("person_id")

                if not person_id:
                    continue

                if person_id in processed_persons:
                    print(f"Skipping duplicate: {person_id}")
                    continue

                processed_persons.add(person_id)

                enriched = enrich_person(person)

                email = enriched.get("email")

                if not email:
                    print("Skipping - no email")
                    continue   

                if email in processed_emails:
                    print(f"Skipping duplicate email: {email}")
                    continue

                processed_emails.add(email)

                if not enriched.get("success"):
                    continue

                print("\nCandidate Found")
                print("-" * 50)

                print(f"Name     : {enriched.get('full_name')}")
                print(f"Company  : {enriched.get('company_name')}")
                print(f"Email    : {enriched.get('email')}")
                print(f"LinkedIn : {enriched.get('linkedin_url')}")

                print("-" * 50)

                choice = input("Send email? (y/n/q): ").lower().strip()

                if choice == "q":
                    print("\n" + "=" * 70)
                    print("Quitting...")
                    print("=" * 70)
                    print(f"\nEmails Sent: {total_sent}")
                    print(f"Skipped: {total_skipped}")
                    return

                if choice != "y":
                    total_skipped += 1
                    continue

                result = send_email(enriched)
                print("\nBrevo Response:")
                print(result)

                total_sent += 1

        except Exception as e:

            print(
                f"Error processing {company_domain}: {e}"
            )

    print("\n" + "=" * 70)
    print("Completed")
    print("=" * 70)

    print(f"Emails Sent : {total_sent}")
    print(f"Skipped     : {total_skipped}")


if __name__ == "__main__":
    main()