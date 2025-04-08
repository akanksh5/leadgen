# 📇 FastAPI Lead Management System

A lightweight and secure lead management backend built with **FastAPI** and **SQLite**. This application allows for public lead submission with resume upload and automated email notifications, alongside an authenticated admin interface to view and update lead statuses.
The design document can be found on the repository.
---

## ✨ Features

- 🔒 **Authentication**: Admin endpoints are protected via HTTP Basic Auth.
- 📤 **Public Lead Submission**: Users can submit their details and upload a resume.
- 📧 **Email Notifications**: Auto-notifies the lead and the admin on submission.
- 📁 **Resume Uploads**: Stores resumes securely in a configurable directory.
- 📊 **Lead Dashboard**: View all submitted leads (admin-only).
- ✅ **State Management**: Track lead status (`PENDING` → `REACHED_OUT`).

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Python3 Virtual Environment
- Gmail account for email notifications (or configure your SMTP)

### Installation

```bash
git clone https://github.com/yourusername/fastapi-leads.git
cd fastapi-leads
pip3 install -r requirements.txt
```

### Configuration

- Make sure these values are set in a .env file which will later be sourced in the config.py
```bash
GMAIL_USER=example@example.com
GMAIL_APP_PASSWORD=your-password-here
ADMIN_EMAIL=example@example.com
UPLOAD_DIR=uploads
DB_FILE =leads.db
AUTH_USERNAME = admin
AUTH_PASSWORD = password
```

### Database Setup
- Since we're using SQLite for this assignment, run the dbinit script to create a file based database.
```bash
python3 dbinit.py
```

### Running the Servers
- We have 2 servers in place. One that can be publicly accessed by the customers and the other
that will be internally hosted on the company's private servers to avoid external access.
- The reason why we have 2 serves instead of one is because the customer facing server can have all the public endpoints. The internal APIs can be hosted on the company's private network with Basic auth enabled.
- We don't really have to involve complex authentication methodologies like OAuth and anything that involves making changes to data should be completely inaccessible to the public.
- Start the customer facing server with the command below.
```bash
uvicorn customer:app --reload              
```
-Start the management hosted server with the command below.
```bash
uvicorn management:app --reload  --port 8080            
```

## 🔧 API Endpoints

### 📥 Public Submission

#### `POST /submit`

Submit a new lead with resume.

**Form Data:**

- `first_name`: string (required)  
- `last_name`: string (required)  
- `email`: email string (required)  
- `resume`: file (required)

**Response:**

```json
{
  "message": "Lead submitted successfully"
}
```


### 🔐 Admin Endpoints (Basic Auth Protected)

All admin endpoints require **HTTP Basic Authentication** using the credentials defined in `config.py`.

---

#### `GET /leads`

Returns a list of all submitted leads.

**Headers:**
Authorization: Basic base64(username:password)

**Response:**

```json
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "resume_path": "uploads/john_resume.pdf",
    "state": "PENDING"
  },
  {
    "id": 2,
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane@example.com",
    "resume_path": "uploads/jane_resume.pdf",
    "state": "REACHED_OUT"
  }
]
```
#### `POST /leads/{lead_id}/reach_out`

Marks a lead as **REACHED_OUT** to indicate the admin has contacted them.

**Path Parameters:**

- `lead_id`: `integer` — ID of the lead to update (required)

**Headers:**
Authorization: Basic base64(username:password)
**Request Example:**

```http
POST /leads/3/reach_out
Authorization: Basic YWRtaW46c2VjdXJlcGFzcw==
```
**Successful Response**
```json
{
  "message": "Lead marked as reached out"
}
```
**Error Response**
```json
{
  "detail": "Lead not found"
}
```

## 📬 Email Integration
- This app uses Gmail SMTP over SSL (port 465) to send emails.

- ✅ A confirmation email to the user upon successful lead submission.

- 🚨 A notification email to the admin about the new lead.
Here's the official link to set up a Gmail App Password:

- 👉 https://myaccount.google.com/apppasswords

### 🔐 How to Set Up a Gmail App Password
- Go to your Google Account Security settings.

- Make sure 2-Step Verification is enabled.

- Once enabled, scroll down to the "App passwords" section.

- Select Mail as the app and Other (Custom name) if you want to label it (e.g., "FastAPI App").

- Click Generate.

- Google will give you a 16-character password. Use this in your config.py or .env file under **GMAIL_APP_PASSWORD** and use your email in **GMAIL_USER**.
