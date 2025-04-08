from pydantic import BaseModel, EmailStr

class Lead(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    resume_path: str
    state: str