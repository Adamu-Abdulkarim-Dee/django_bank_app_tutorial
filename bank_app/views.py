from django.shortcuts import render, redirect 
from .forms import TransactionForm, DepositForm
from django.contrib.auth.decorators import user_passes_test 
from .models import Deposit, Transaction 
from accounts.models import Account 
import random

def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            
            sender_account = Account.objects.get(user=request.user)
            receiver_account = Account.objects.get(account_number=transaction.account_number)
            
            # Check if sender's balance is sufficient
            if sender_account.account_balance >= transaction.amount:
                sender_account.account_balance -= transaction.amount
                
                receiver_account.account_balance += transaction.amount
                
                sender_account.save()
                receiver_account.save()
                
                transaction.sender = sender_account.user
                transaction.receiver = receiver_account.user
                transaction.reference_number = random.randint(1000000000, 9999999999)  # 10-digit random number
                transaction.status = 'Success'
                transaction.save()
                return redirect('transaction_success')
            else:
                form.add_error('amount', 'Insufficient funds.')
    else:
        form = TransactionForm()

    return render(request, 'create_transaction.html', {'form': form})

def transaction_success(request):
    return render(request, 'transaction_success.html')


@user_passes_test(lambda u: u.is_superuser)
def create_deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            
            receiver_account = Account.objects.get(account_number=deposit.account_number)
            
            # Add the deposit amount to the receiver's account balance
            if receiver_account.account_balance is None:
                receiver_account.account_balance = 0
            
            receiver_account.account_balance += deposit.amount
            receiver_account.save()
            
            deposit.sender = request.user
            deposit.receiver = receiver_account.user
            deposit.status = 'Success'
            deposit.save()
            return redirect('transaction_success')
    else:
        form = DepositForm()
    return render(request, 'create_deposit.html', {'form': form})
