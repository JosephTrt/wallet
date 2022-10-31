from django.db import models

from apps.account.models import Account
from apps.users.models import User

# Create your models here.
class Transaction(models.Model):

    OPERATION_CHOICES =(
        ('1', 'Deposit'),
        ('2', 'Extraction'),
        ('3', 'Transfer')
    )


    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha'
    )
    credit_account = models.ForeignKey(
        Account,
        null=True,
        on_delete=models.CASCADE,
        related_name='Acreditaciones',
        verbose_name='Destino'
    )
    debit_account = models.ForeignKey(
        Account,
        null=True,
        on_delete=models.CASCADE,
        related_name='Extracciones',
        verbose_name='Partida'
    )
    amount = models.PositiveIntegerField(
        verbose_name='Monto'
    )
    operation_type = models.CharField(
        max_length=1,
        choices=OPERATION_CHOICES
    )

    class Meta:
        verbose_name = 'Transacción'
        verbose_name_plural = 'Tracciones'
    