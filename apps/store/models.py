from django.db import models


class StoreModel(models.Model):
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        db_table = 'store_store'

    name = models.CharField(verbose_name='Название', max_length=255)
