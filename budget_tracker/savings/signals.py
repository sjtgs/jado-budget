from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SavingsTransaction, SavingsAccount, SavingsGoal
from django.db import transaction


@receiver(post_save, sender=SavingsTransaction)
def update_balances(sender, instance, created, **kwargs):
    if not created:
        return

    with transaction.atomic():
        account = instance.account
        goal = instance.goal

        if instance.transaction_type == 'DEPOSIT':
            account.balance += instance.amount
            account.save()

            if goal:
                goal.current_amount += instance.amount
                goal.save()

        elif instance.transaction_type == 'WITHDRAWAL':
            account.balance -= instance.amount
            account.save()

            if goal:
                goal.current_amount -= instance.amount
                goal.save()

        elif instance.transaction_type == 'TRANSFER':
            # Transfer must be implemented with two transactions.
            # We'll handle it later properly.
            pass
