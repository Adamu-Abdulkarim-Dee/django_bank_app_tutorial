from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.conf import settings

class CustomUser(AbstractUser):
    username = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    account_pin = models.CharField(max_length=4, blank=True, null=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, 
    blank=True, null=True, default=0)

    def __str__(self):
        return str(f"Account {self.account_number} for {self.user.username}")
