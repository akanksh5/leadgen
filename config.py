import os
from dotenv import load_dotenv

load_dotenv()  # Load .env into environment

class Settings:
    GMAIL_USER: str = os.getenv("GMAIL_USER")
    GMAIL_APP_PASSWORD: str = os.getenv("GMAIL_APP_PASSWORD")
    ADMIN_EMAIL: str = os.getenv("ADMIN_EMAIL", "default@example.com")
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "uploads")
    DB_FILE: str = os.getenv("DB_FILE", "leads.db")
    AUTH_USERNAME: str = os.getenv("AUTH_USERNAME")
    AUTH_PASSWORD: str = os.getenv("AUTH_PASSWORD")

# Create a single instance to use everywhere
settings = Settings()
