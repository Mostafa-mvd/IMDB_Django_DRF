from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models
from . import tasks


@receiver(post_save, sender=models.Movie)
def send_movie_creation_email(sender, instance, created, **kwargs):
    if created:
        serialized_movie_instance = {
            'title': instance.title,
            'date_posted': instance.date_posted,
            'released_date': instance.released_date,
        }
        
        return tasks.send_email_to_all.delay(**serialized_movie_instance)
