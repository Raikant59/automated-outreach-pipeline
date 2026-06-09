# Automated Outreach Pipeline

## Overview

Automated Outreach Pipeline is a Python-based lead generation and outreach system that:

1. Finds companies similar to a target company using Gemini AI.
2. Searches for people working at those companies using the Prospeo Search Person API.
3. Enriches prospect data using the Prospeo Enrich Person API.
4. Allows manual approval before sending emails.
5. Sends personalized outreach emails using Brevo.

---

## Workflow

```text
User Domain
    ↓
Gemini AI
    ↓
Similar Company Domains
    ↓
Prospeo Search Person API
    ↓
Prospect Information
    ↓
Prospeo Enrich Person API
    ↓
Verified Contact Information
    ↓
User Approval (Y/N)
    ↓
Brevo Email API
    ↓
Outreach Email Sent
```

---

## Project Structure

```text
automated-outreach-pipeline/

│
├── main.py
│
├── services/
│   ├── __init__.py
│   ├── finder.py
│   ├── search_people.py
│   ├── enrich.py
│   └── brevo.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## Features

* Similar company discovery using Gemini AI
* Prospect discovery using Prospeo
* Prospect enrichment using Prospeo
* Personalized email generation
* Manual approval before sending emails
* Duplicate protection
* Pagination support
* JSON-based API integration

---

## Environment Variables

Create a `.env` file in the root directory.

```env
GEMINI_API_KEY=your_gemini_api_key

PROSPEO_API_KEY=your_prospeo_api_key

BREVO_API_KEY=your_brevo_api_key
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>

cd automated-outreach-pipeline
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python main.py
```

Example:

```text
Enter company domain:
google.com
```

The system will:

1. Find similar companies.
2. Search for prospects.
3. Enrich prospect information.
4. Display prospect details.
5. Ask:

```text
Send email? (y/n/q)
```

6. Send email through Brevo if approved.

---

## APIs Used

### Gemini AI

Used for identifying similar companies.

### Prospeo Search Person API

Used for finding prospects from company domains.

### Prospeo Enrich Person API

Used for retrieving verified contact information.

### Brevo SMTP API

Used for sending personalized outreach emails.

---

## Duplicate Protection

The application prevents duplicate outreach using:

* person_id tracking
* email tracking

This prevents sending multiple emails to the same contact.

---

## Security Notes

* Never commit your `.env` file.
* Never expose API keys publicly.
* Use verified sender emails in Brevo.
* Respect email outreach regulations and privacy laws.

---

## Future Improvements

* Multi-Template Outreach System
* AI-Powered Email Generation
* Bulk Outreach
* Multi-Channel Outreach

---

## Author

Raikant Chaudhary

Built using Python, Gemini AI, Prospeo, and Brevo.
Built with ❤️
