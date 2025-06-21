from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model, user_logged_in, user_logged_out
import logging

from django.utils.timezone import now

from accounts.models import CustomUser, Profile

User = get_user_model()


@receiver(user_logged_in)
def on_user_login(sender, request, user, **kwargs):
    print(f"{user.email} logged in at {now()}")


@receiver(user_logged_out)
def on_user_logout(sender, request, user, **kwargs):
    print(f"{user.email} logged out at {now()}")


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)

