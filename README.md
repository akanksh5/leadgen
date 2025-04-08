# 📇 FastAPI Lead Management System

A lightweight and secure lead management backend built with **FastAPI** and **SQLite**. This application allows for public lead submission with resume upload and automated email notifications, alongside an authenticated admin interface to view and update lead statuses.

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
- Start the customer facing server with the command below.
```bash
uvicorn customer:app --reload              
```
-Start the management hosted server with the command below.
```bash
uvicorn management:app --reload              
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

