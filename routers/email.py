from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

root = APIRouter(prefix="/sendEmail",
                 tags=["sendEmail"],
                 responses={404: {status.HTTP_404_NOT_FOUND: "Contact not found"}})

@root.post("/", response_model=dict)
async def send_email(email_data: dict):
    return email_data