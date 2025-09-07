from flask import Flask, request, jsonify
from services.openai_service import qualify_lead
from services.crm_service import push_to_hubspot
from services.notify_service import notify_slack
from db import save_lead

app = Flask(__name__)

@app.route("/lead", methods=["POST"])
def handle_lead():
    """
    Receive a new lead from website/chat form
    Example POST body:
    {
        "name": "John Ezekiel",
        "email": "john@siriusb.com",
        "message": "I need solar panels for my home, budget is $5000"
    }
    """
    data = request.json

    # Step 1: Qualify lead with AI
    qualification = qualify_lead(data)

    # Step 2: Save to DB
    lead_id = save_lead(data, qualification)

    # Step 3: Push to HubSpot
    push_to_hubspot(data, qualification)

    # Step 4: Notify Slack
    notify_slack(data, qualification)

    return jsonify({"lead_id": lead_id, "qualification": qualification})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
