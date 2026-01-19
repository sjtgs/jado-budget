from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class MonthlyBudget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.DateField()  # use the first day of month
    income_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    needs_budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    wants_budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    savings_budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    debts_budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    investments_budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'month')
        ordering = ['-month']

    def __str__(self):
        return f"{self.user.username} - {self.month.strftime('%B %Y')}"


class MonthlySpend(models.Model):
    SPEND_TYPES = [
        ('NEEDS', 'Needs'),
        ('WANTS', 'Wants'),
        ('SAVINGS', 'Savings'),
        ('DEBTS', 'Debts'),
        ('INVESTMENTS', 'Investments'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.DateField()
    spend_type = models.CharField(max_length=15, choices=SPEND_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
