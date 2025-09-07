# LeadBot

LeadBot is a Flask-based microservice that integrates:
- **OpenAI** for lead qualification
- **HubSpot CRM** for lead management
- **Slack/Twilio** for notifications
- **MySQL** for persistence

## Project Structure
\`\`\`
leadbot/
│── app.py                # Flask app + REST routes
│── db.py                 # MySQL connection + ORM helpers
│── services/
│    ├── openai_service.py    # Lead qualification logic
│    ├── crm_service.py       # HubSpot REST integration
│    ├── notify_service.py    # Slack/Twilio notifications
│── models.sql            # DB schema
│── requirements.txt
│── Dockerfile
│── .env.example          # API keys + DB creds
│── README.md             # Project documentation
\`\`\`

## Setup

1. Create a virtual environment and install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

2. Set environment variables using \`.env.example\`.

3. Run the app:
   \`\`\`bash
   python app.py
   \`\`\`

4. Or build and run with Docker:
   \`\`\`bash
   docker build -t leadbot .
   docker run -p 5000:5000 --env-file .env leadbot
   \`\`\`

---
EOF