import mysql.connector
import os

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )

def save_lead(data, qualification):
    db = get_db()
    cursor = db.cursor()
    sql = """
    INSERT INTO leads (name, email, message, score, summary, budget, problem, company, role)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(sql, (
        data.get("name"), data.get("email"), data.get("message"),
        qualification.get("score"), qualification.get("summary"),
        qualification.get("budget"), qualification.get("problem"),
        qualification.get("company"), qualification.get("role")
    ))
    db.commit()
    lead_id = cursor.lastrowid
    cursor.close()
    db.close()
    return lead_id
