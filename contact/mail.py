from django.core.mail import send_mail
from pathlib import Path
from django.conf import settings
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))


def contact_response(name, email):
    """Sends a response to a saved email in the database"""
    subject = "Thank you for reaching out!"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    message = """
    Dear {},

    Thank you for reaching out to me through my portfolio website. I appreciate your interest in my work and I am thrilled to hear from you.

    I have received your message and I am currently reviewing your inquiry. I will get back to you as soon as possible to answer any questions you may have or to discuss your project further.

    In the meantime, please feel free to explore my portfolio and get a better sense of my style and capabilities. If you have any urgent matters, please don't hesitate to send me further emails.

    Thank you again for taking the time to reach out to me. I look forward to the opportunity to work with you and bring your ideas to life.

    Best regards,
    {}
    """.format(name, os.getenv("FULL_NAME"))

    send_mail(
        subject,
        message,
        email_from,
        recipient_list,
        fail_silently=True,
    )

    return True

def personal_message(name, email, message):
    """Sends a response to a saved email to myself"""
    subject = "You have a message!"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [os.getenv("PERSONAL_EMAIL")]
    message = """
    Name: {},

    Email: {},

    Message: {}

    An automated response has been sent out.
    """.format(name, email, message)

    send_mail(
        subject,
        message,
        email_from,
        recipient_list,
        fail_silently=True,
    )

    return True