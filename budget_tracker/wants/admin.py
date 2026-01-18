from django.contrib import admin
from .models import WantCategory, WantTransaction


@admin.register(WantCategory)
class WantCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(WantTransaction)
class WantTransactionAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'transaction_date', 'reference')
    list_filter = ('category', 'transaction_date')
    date_hierarchy = 'transaction_date'
