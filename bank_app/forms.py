from django import forms
from .models import Transaction, Deposit

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'account_number']

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount', 'account_number']