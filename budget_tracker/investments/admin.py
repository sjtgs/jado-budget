from django.contrib import admin
from .models import Investment, InvestmentTransaction


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'investment_type', 'created_at')
    search_fields = ('name',)


@admin.register(InvestmentTransaction)
class InvestmentTransactionAdmin(admin.ModelAdmin):
    list_display = ('investment', 'transaction_type', 'amount', 'units', 'transaction_date')
    list_filter = ('transaction_type', 'transaction_date')
