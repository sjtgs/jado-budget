from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Income
from allocations.models import Allocation


@receiver(post_save, sender=Income)
def create_allocation(sender, instance, created, **kwargs):
    if not created:
        return

    Allocation.objects.create(
        user=instance.user,
        income=instance,
        needs_allocated=instance.amount * 0.5,
        wants_allocated=instance.amount * 0.2,
        savings_allocated=instance.amount * 0.3 * 0.5,
        debts_allocated=instance.amount * 0.3 * 0.25,
        investments_allocated=instance.amount * 0.3 * 0.25,
    )
