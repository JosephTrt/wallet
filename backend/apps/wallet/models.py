from django.db import models

from apps.users.models import User
from apps.account.models import Account
from apps.transaction.models import Transaction


# Create your models here.
class Wallet(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE
    )
    transaction = models.ManyToManyField(
        Transaction,
        null=True,
        related_name='History'
    )

    class Meta:
        verbose_name = 'Villetera'
        verbose_name_plural = 'Villeteras'
    
    
    def __str__(self) -> str:
        return self.user.username