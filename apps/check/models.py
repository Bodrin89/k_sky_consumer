from django.db import models

from apps.store.models import StoreModel


class CheckModel(models.Model):
    class Meta:
        verbose_name = 'Проверка'
        verbose_name_plural = 'Проверки'
        db_table = 'check_check'

    transaction_id = models.PositiveIntegerField(unique=True, verbose_name='ID транзакции')
    timestamp = models.DateTimeField(verbose_name='время совершения покупки')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='общая сумма чека')
    nds_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма НДС')
    tips_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма чаевых')
    payment_method = models.CharField(max_length=255, verbose_name='способ оплаты')
    place = models.ForeignKey(StoreModel, on_delete=models.CASCADE, null=True, related_name='checks')
