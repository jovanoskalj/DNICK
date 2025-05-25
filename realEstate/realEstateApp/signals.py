from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from .models import *

#Кога еден оглас/недвижнина ќе се означи како
# продадена, потребно е сите агенти поврзани со
# неа да ја инкрементираат својата продажба
@receiver(pre_save, sender=RealEstate)
def my_handler(sender, instance, **kwargs):
    old_instance = RealEstate.objects.filter(id=instance.id).first()
    if old_instance:
        if instance.isSold != old_instance.isSold:
            array = RealEstateAgent.objects.filter(real_estate=old_instance).all()
            for a in array:
                a.agent.num_sells += 1
                a.agent.save()

