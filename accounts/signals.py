from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model, user_logged_in, user_logged_out
import logging

from django.utils.timezone import now

User = get_user_model()


@receiver(user_logged_in)
def on_user_login(sender, request, user, **kwargs):
    print(f"{user.email} logged in at {now()}")


@receiver(user_logged_out)
def on_user_logout(sender, request, user, **kwargs):
    print(f"{user.email} logged out at {now()}")
