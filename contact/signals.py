from django.dispatch import receiver
from django.db.models.signals import post_save
from contact.models import Contact
from contact.mail import contact_response, personal_message


@receiver(post_save, sender=Contact)
def send_response(sender, instance, created, **kwargs):
    if created:
        try:
            # Send response to send of message
            contact_response(instance.name, instance.email)

            # Send notification to self
            personal_message(instance.name, instance.email, instance.message)
        except:
            pass
