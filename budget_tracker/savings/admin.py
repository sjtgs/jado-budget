from django.contrib import admin
from .models import SavingsAccount, SavingsGoal, SavingsTransaction


@admin.register(SavingsAccount)
class SavingsAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'created_at')
    search_fields = ('name',)


@admin.register(SavingsGoal)
class SavingsGoalAdmin(admin.ModelAdmin):
    list_display = ('name', 'target_amount', 'current_amount', 'due_date')
    search_fields = ('name',)


@admin.register(SavingsTransaction)
class SavingsTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'amount', 'account', 'goal', 'transaction_date')
    list_filter = ('transaction_type', 'transaction_date')
    date_hierarchy = 'transaction_date'
