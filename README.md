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
pip install -r requirements.txt
