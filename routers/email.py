from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI()

@app.post("/send-email/")
async def send_email(email_data: dict):
    # Extract email data
    email = email_data.email
    subject = email_data.subject
    body = email_data.body

    # Email configuration
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'
    smtp_server = 'smtp.example.com'
    smtp_port = 587  # SMTP port (587 is the default for TLS)

    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send email
    server.sendmail(sender_email, email, message.as_string())

    # Close connection
    server.quit()

    return {"message": "Email sent successfully"}