import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account, CustomUser

@receiver(post_save, sender=CustomUser)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        account_number = ''.join(random.choices('0123456789', k=10))
        Account.objects.create(user=instance, account_number=account_number)
