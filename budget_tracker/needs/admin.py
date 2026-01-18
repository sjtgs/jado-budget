from django.contrib import admin
from .models import NeedCategory, NeedTransaction


@admin.register(NeedCategory)
class NeedCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(NeedTransaction)
class NeedTransactionAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'transaction_date', 'reference')
    list_filter = ('category', 'transaction_date')
    date_hierarchy = 'transaction_date'
