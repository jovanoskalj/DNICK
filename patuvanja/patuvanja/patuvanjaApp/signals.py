from random import random

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import *


@receiver(pre_delete, sender=Guide)
def my_handler(sender, instance, **kwargs):
    travel = Travel.objects.filter(guide=instance)

    other_guides = Guide.objects.exlcude(id=instance.id).all()

    for travel in travel:
        new_guide = random.choice(other_guides)
        travel.guide = new_guide
        travel.save()
