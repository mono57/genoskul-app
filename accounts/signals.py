from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Speciality
from forum.models import Forum


@receiver(post_save, sender=Speciality)
def post_save_speciality_create_forum(sender, instance, created, **kwargs):
    if created:
        Forum.objects.create(type=instance)
