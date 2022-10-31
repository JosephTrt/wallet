from django.db import models

from apps.users.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    account_number = models.PositiveBigIntegerField(
        default=0,
        unique=True,
        verbose_name='Numero de cuenta'
    )
    alias = models.CharField(
        max_length=30,
        unique=True
    )
    amount = models.PositiveIntegerField(
        default=0,
        verbose_name='Saldo'
    )
    create_date = models.DateField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
    
    def __str__(self) -> str:
        return self.account_number
    