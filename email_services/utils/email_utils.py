from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from django.conf import settings


def send_email(subject, body, userEmails):
    msg = MIMEMultipart()
    msg['From'] = settings.FROM_ALIAS
    msg['Subject'] = subject

    try:
        part = MIMEText(body, 'html')
        msg.attach(part)
        msg['To'] = ", ".join(userEmails)
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.starttls()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        for userEmail in userEmails:
            server.sendmail(settings.FROM_ALIAS, userEmail , msg.as_string())
        server.quit()
        return {
            "Message": "Germination Report Email Sent Successfully!",
            "Status": "Success"
        }
    except Exception as e:
        return({
            "Message": f"Failed to send email: {e}",
            "Status": "Failed"
        })
    

def send_notification(subject, body, userEmail):
    msg = MIMEMultipart()
    msg['From'] = settings.FROM_ALIAS
    msg['Subject'] = subject

    try:
        part = MIMEText(body, 'html')
        msg.attach(part)
        msg['To'] = userEmail
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.starttls()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.sendmail(settings.FROM_ALIAS, userEmail , msg.as_string())
        server.quit()
        return {
            "message": "Email Sent Successfully!",
            "status": "Success"
        }
    except Exception as e:
        return({
            "message": f"Failed to send email: {e}",
            "status": "Failed"
        })