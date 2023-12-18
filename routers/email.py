from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

root = APIRouter(prefix="/sendEmail",
                 tags=["sendEmail"],
                 responses={404: {status.HTTP_404_NOT_FOUND: "Contact not found"}})

@root.post("/", response_model=dict)
async def send_email(email_data: dict):
    load_dotenv()
        
    msg = MIMEMultipart()
    msg['From'] = os.getenv('USER_EMAIL')
    msg['To'] = email_data["email"]
    msg['Subject'] = "Thanks for use my program"
    
    tMessage = f'Hola mucho gusto'
    
    email = MIMEText(tMessage,"plain")
    
    msg.attach(email)
    
    mailServer = smtplib.SMTP(os.getenv('SMTP_SSL'), 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(os.getenv('USER_EMAIL'), os.getenv('PASSWORD_EMAIL'))
    
    mailServer.sendmail(os.getenv('USER_EMAIL'), email_data["email"], msg.as_string())
    
    mailServer.close()
    
    return {"message": "email send"}