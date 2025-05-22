import random
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import *


@receiver(pre_delete, sender=Guide)
def my_handler(sender,instance, **kwargs):
    travels = Travel.objects.filter(guide=instance)

    other_guides = Guide.objects.exclude(id=instance.id).all()

    for travel in travels:
        new_guide = random.choice(other_guides)
        travel.guide = new_guide
        travel.save()