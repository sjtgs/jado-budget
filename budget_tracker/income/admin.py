from django.contrib import admin
from .models import IncomeSource, IncomeTransaction


@admin.register(IncomeSource)
class IncomeSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(IncomeTransaction)
class IncomeTransactionAdmin(admin.ModelAdmin):
    list_display = ('source', 'amount', 'received_date', 'created_at')
    list_filter = ('source', 'received_date')
    date_hierarchy = 'received_date'
