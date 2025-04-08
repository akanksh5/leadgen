from typing import List
import sqlite3
import secrets
from models import Lead
from config import settings
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials



app = FastAPI()
security = HTTPBasic()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username,settings.AUTH_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, settings.AUTH_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return credentials.username

@app.get("/leads", response_model=List[Lead])
def get_leads(user: str = Depends(authenticate)):
    with sqlite3.connect(settings.DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, first_name, last_name, email, resume_path, state FROM leads")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]

@app.post("/leads/{lead_id}/reach_out")
def mark_reached_out(lead_id: int, user: str = Depends(authenticate)):
    with sqlite3.connect(settings.DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE leads SET state = 'REACHED_OUT' WHERE id = ?", (lead_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Lead not found")
        conn.commit()
    return {"message": "Lead marked as reached out"}