from django.contrib import admin
from .models import Transaction, Deposit

admin.site.register(Transaction)
admin.site.register(Deposit)
