from django.contrib import admin
from .models import Debt, DebtTransaction


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('name', 'principal_amount', 'interest_rate', 'due_date')
    search_fields = ('name',)


@admin.register(DebtTransaction)
class DebtTransactionAdmin(admin.ModelAdmin):
    list_display = ('debt', 'transaction_type', 'amount', 'transaction_date')
    list_filter = ('transaction_type', 'transaction_date')
