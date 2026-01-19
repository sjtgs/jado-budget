from django.db import models
from django.contrib.auth.models import User
from income.models import Income
from needs.models import NeedCategory
from wants.models import WantCategory
from savings.models import SavingsAccount, SavingsGoal
from debts.models import Debt
from investments.models import Investment


class Allocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.OneToOneField(Income, on_delete=models.CASCADE)

    needs_allocated = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    wants_allocated = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    savings_allocated = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    debts_allocated = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    investments_allocated = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def total_allocated(self):
        return (
            self.needs_allocated +
            self.wants_allocated +
            self.savings_allocated +
            self.debts_allocated +
            self.investments_allocated
        )

    def __str__(self):
        return f"Allocation for {self.income.amount}"


class AllocationSpend(models.Model):
    ALLOCATION_TYPES = [
        ('NEEDS', 'Needs'),
        ('WANTS', 'Wants'),
        ('SAVINGS', 'Savings'),
        ('DEBTS', 'Debts'),
        ('INVESTMENTS', 'Investments'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    allocation = models.ForeignKey(Allocation, on_delete=models.CASCADE)
    allocation_type = models.CharField(max_length=15, choices=ALLOCATION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.allocation_type} - {self.amount}"
