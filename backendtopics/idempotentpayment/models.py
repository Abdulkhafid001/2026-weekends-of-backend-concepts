from django.db import models


class Payment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'
    username = models.CharField()
    idempotent_key = models.CharField(unique=True, blank=False, null=False)
    total = models.IntegerField()
    transaction_status = models.CharField(choices=Status.choices, default='Pending')

    def __str__(self):
        return self.username
