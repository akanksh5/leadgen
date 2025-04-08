📇 FastAPI Lead Management System
A lightweight and secure lead management backend built with FastAPI and SQLite. This application allows for public lead submission with resume upload and automated email notifications, alongside an authenticated admin interface to view and update lead statuses.

✨ Features
🔒 Authentication: Admin endpoints are protected via HTTP Basic Auth.

📤 Public Lead Submission: Users can submit their details and upload a resume.

📧 Email Notifications: Auto-notifies the lead and the admin on submission.

📁 Resume Uploads: Stores resumes securely in a configurable directory.

📊 Lead Dashboard: View all submitted leads (admin-only).

✅ State Management: Track lead status (PENDING → REACHED_OUT).

🚀 Getting Started
Prerequisites
Python 3.9+

Gmail account for email notifications (or configure your SMTP)

Installation
bash
Copy
Edit
git clone https://github.com/yourusername/fastapi-leads.git
cd fastapi-leads
pip install -r requirements.txt
Configuration
Create a config.py file with the following settings:

python
Copy
Edit
from pydantic import BaseSettings

class Settings(BaseSettings):
    UPLOAD_DIR: str = "uploads"
    DB_FILE: str = "leads.db"
    GMAIL_USER: str
    GMAIL_APP_PASSWORD: str
    ADMIN_EMAIL: str
    AUTH_USERNAME: str = "admin"
    AUTH_PASSWORD: str = "securepassword"

settings = Settings()
Use environment variables or a .env file to keep sensitive data secure.

Initialize the Database
The database is automatically initialized when the server starts.

🔧 API Endpoints
Public Endpoint
POST /submit
Submit a lead with resume upload.

Form Data:

first_name: str

last_name: str

email: str (validated)

resume: File (PDF, DOC, etc.)

Response:

json
Copy
Edit
{ "message": "Lead submitted successfully" }
Admin Endpoints (HTTP Basic Auth Protected)
GET /leads
Get all submitted leads.

Headers:

http
Copy
Edit
Authorization: Basic base64encoded(username:password)
Response:

json
Copy
Edit
[
  {
    "id": 1,
    "first_name": "Alice",
    "last_name": "Smith",
    "email": "alice@example.com",
    "resume_path": "uploads/alice_resume.pdf",
    "state": "PENDING"
  }
]
POST /leads/{lead_id}/reach_out
Mark a lead as reached out.

Response:

json
Copy
Edit
{ "message": "Lead marked as reached out" }
📂 Project Structure
bash
Copy
Edit
.
├── main.py              # FastAPI application
├── config.py            # Configuration file
├── models.py            # Pydantic model(s)
├── requirements.txt     # Dependencies
└── uploads/             # Directory for storing resumes
📬 Email Integration
This app uses Gmail SMTP (SSL, port 465) to send:

A thank-you email to the user

A new lead alert to the admin

Make sure to enable App Passwords in your Google account.

🔐 Security Notes
Admin routes are protected using FastAPI's HTTPBasic and secrets.compare_digest.

Use HTTPS in production to keep credentials secure.

Do not expose .env or config.py with real credentials.

🧪 Running the App
bash
Copy
Edit
uvicorn main:app --reload
Then access:

Submit Lead: POST http://localhost:8000/submit

Admin API: http://localhost:8000/leads

📌 Todo
 Add JWT-based authentication

 Resume file format validation

 Frontend dashboard for admins

 Pagination for /leads

📃 License
MIT License

