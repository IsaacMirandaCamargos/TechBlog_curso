from django.core.mail import EmailMessage
import os

def send_welcome_email(email):
    email_message = EmailMessage(
        subject="Bem vindo ao TECH Blog",
        body="Aproveite para aprender enquanto se aventura.",
        to=[email],
        from_email=os.getenv("SENDINBLUE_EMAIL_HOST")
    )
    email_message.template_id = 1
    email_message.send()