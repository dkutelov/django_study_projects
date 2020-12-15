from django.core.mail import send_mail
from rest_open_course_appointments import settings
from rest_open_course_appointments.celery import app


@app.task
def email_to_customer(user_name, recipient):
    subject = "Thank you for contacting us"
    message = f'Hello, {user_name}! We, received your question and we will answer you as fast as we can!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [recipient,]
    send_mail(subject, message, email_from, recipient_list)


@app.task
def email_to_admin(recipient, content):
    subject = f"You have new question from {recipient}"
    message = f'{content}'
    email_from = recipient
    recipient_list = [settings.EMAIL_HOST_USER,]
    send_mail(subject, message, email_from, recipient_list)