from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db.models import Sum
from datetime import date

from .models import NeedTransaction
from budget.models import MonthlyBudget, MonthlySpend
from django.db.models.signals import post_save

def month_start(d):
    return d.replace(day=1)


@receiver(pre_save, sender=NeedTransaction)
def enforce_needs_budget(sender, instance, **kwargs):
    month = month_start(instance.transaction_date)

    budget = MonthlyBudget.objects.filter(
        user=instance.user,
        month=month
    ).first()

    if not budget:
        raise ValidationError(
            "No monthly budget found. Add income before recording expenses."
        )

    spent = MonthlySpend.objects.filter(
        user=instance.user,
        month=month,
        spend_type='NEEDS'
    ).aggregate(total=Sum('amount'))['total'] or 0

    remaining = budget.needs_budget - spent

    if instance.amount > remaining:
        raise ValidationError(
            f"Needs budget exceeded. Remaining: {remaining}"
        )


@receiver(post_save, sender=NeedTransaction)
def record_needs_spend(sender, instance, created, **kwargs):
    if not created:
        return

    month = month_start(instance.transaction_date)

    MonthlySpend.objects.create(
        user=instance.user,
        month=month,
        spend_type='NEEDS',
        amount=instance.amount
    )