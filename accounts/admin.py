from django.contrib import admin
from .models import Account, CustomUser

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'account_balance', 'user')
    search_fields = ('account_number', 'user__email')
    list_filter = ('user',)


admin.site.register(CustomUser)