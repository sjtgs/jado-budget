from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from decimal import Decimal


class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    investment_type = models.CharField(max_length=50)  # stocks, mutual funds, crypto etc
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'name')
        ordering = ['name']

    def __str__(self):
        return self.name

    def total_units(self):
        buys = self.investmenttransaction_set.filter(transaction_type='BUY').aggregate(total=Sum('units'))['total'] or Decimal('0')
        sells = self.investmenttransaction_set.filter(transaction_type='SELL').aggregate(total=Sum('units'))['total'] or Decimal('0')
        return buys - sells


class InvestmentTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
        ('DIVIDEND', 'Dividend'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment = models.ForeignKey(Investment, on_delete=models.PROTECT)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    units = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    price_per_unit = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    transaction_date = models.DateField()
    reference = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-transaction_date']

    def __str__(self):
        return f"{self.investment.name} - {self.transaction_type} - {self.amount}"
