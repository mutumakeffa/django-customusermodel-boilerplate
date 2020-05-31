# This is a signal that gets fired after an object is saved
# in our case, the post_save is a signal that will get fired up when a user is created

from django.db.models.signals import post_save 

# The sender is what sends the signal and in this case it will be the custom user we created
from .models import CustomUser

# We will need to create the receiver, which is a fxn that receives the signal and does some tasks
from django.dispatch import receiver

# We will create a profile from our function
from .models import Profile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) # create a profile for the user instance created



@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()