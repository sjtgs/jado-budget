from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from datetime import date
from .models import Income
from budget.models import MonthlyBudget


def month_start(d):
    return d.replace(day=1)


@receiver(post_save, sender=Income)
def update_monthly_budget(sender, instance, created, **kwargs):
    if not created:
        return

    month = month_start(instance.date)

    income_total = Income.objects.filter(
        user=instance.user,
        date__year=month.year,
        date__month=month.month
    ).aggregate(total=Sum('amount'))['total'] or 0

    needs = income_total * 0.5
    wants = income_total * 0.2
    savings = income_total * 0.3 * 0.5
    debts = income_total * 0.3 * 0.25
    investments = income_total * 0.3 * 0.25

    MonthlyBudget.objects.update_or_create(
        user=instance.user,
        month=month,
        defaults={
            'income_total': income_total,
            'needs_budget': needs,
            'wants_budget': wants,
            'savings_budget': savings,
            'debts_budget': debts,
            'investments_budget': investments,
        }
    )
