import shutil
import sqlite3
import smtplib
import os
from models import Lead
from email.message import EmailMessage
from config import settings
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic
from pydantic import EmailStr


app = FastAPI()
security = HTTPBasic()

if not os.path.exists(settings.UPLOAD_DIR):
    os.makedirs(settings.UPLOAD_DIR)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def send_email(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = settings.GMAIL_USER
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(settings.GMAIL_USER, settings.GMAIL_APP_PASSWORD)
        server.send_message(msg)

@app.post("/submit")
def submit_lead(
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: EmailStr = Form(...),
    resume: UploadFile = File(...),
):
    file_location = f"{settings.UPLOAD_DIR}/{resume.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)
    print("hi")
    with sqlite3.connect(settings.DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO leads (first_name, last_name, email, resume_path)
            VALUES (?, ?, ?, ?)
        """, (first_name, last_name, email, file_location))
        conn.commit()
    print("bye")
    send_email(email, "Thanks for your submission", "We received your lead.")
    send_email(settings.ADMIN_EMAIL, "New lead submitted", f"New lead from {first_name} {last_name}, email: {email}")

    return {"message": "Lead submitted successfully"}

