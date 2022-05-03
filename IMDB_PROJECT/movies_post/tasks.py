import smtplib
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from django.conf import settings

from celery import shared_task


@shared_task
def send_email_to_all(title, date_posted, released_date):
    
    user_model = get_user_model()
    users_have_email_qs = user_model.objects.exclude(email__exact='').values_list("email", flat=True)
    email_message = f"The {title} is released, let's see review of each people."
    
    try:
        send_mail(
            subject=title,
            message=email_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=users_have_email_qs,
            fail_silently=False)

        return True
    except smtplib.SMTPException as exc:
        print(exc)
        return False
