from django.urls import path
from . import views

urlpatterns = [
    path('create_transaction/', views.create_transaction, name='create_transactions'),
    path('transaction_success/', views.transaction_success, name='transaction_success'),
    path('create_deposit/', views.create_deposit, name='create_deposit'),
]
