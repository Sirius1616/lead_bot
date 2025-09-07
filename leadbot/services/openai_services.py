import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def qualify_lead(lead):
    prompt = f"""
    You are a sales assistant. 
    Analyze this lead:
    Name: {lead.get("name")}
    Email: {lead.get("email")}
    Message: {lead.get("message")}

    Extract answers for:
    - Company/Role (if mentioned)
    - Budget/Spend
    - Main Problem

    Score lead 0-100 (higher = more qualified).
    Return valid JSON only with fields: company, role, budget, problem, score, summary.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=300,
        temperature=0
    )

    try:
        return eval(response["choices"][0]["message"]["content"])  # Convert JSON string to dict
    except:
        return {"company": None, "role": None, "budget": None, "problem": None, "score": 0, "summary": "Parsing error"}
