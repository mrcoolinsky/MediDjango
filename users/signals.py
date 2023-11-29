from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from main.models import Patient, Address


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance)
        print('Profile created')
'''
    address = Address.objects.get_or_create(user=instance)
    address.Street = instance.Street
    address.Number = instance.Number
    address.Zip_code = instance.Zip_code
    address.City = instance.City
    address.save()
'''

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if not created:
        instance.Patient.save()
        #instance.address.save()
        print('Profile updated')
