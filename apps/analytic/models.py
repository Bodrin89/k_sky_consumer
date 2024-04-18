from django.db import models


class PlaceAnalyticModel(models.Model):
    class Meta:
        verbose_name = 'Аналитика по местам покупки'
        verbose_name_plural = 'Аналитики по местам покупки'
        db_table = 'analytic_place_analytic'

    place_id = models.IntegerField()
    place_name = models.CharField(max_length=255)
    total_purchases = models.PositiveIntegerField()
    average_receipt = models.FloatField()
    taxes_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_nds = models.DecimalField(max_digits=10, decimal_places=2)
    total_tips = models.DecimalField(max_digits=10, decimal_places=2)


class CategoryAnalyticModel(models.Model):
    class Meta:
        verbose_name = 'Аналитика по категориям'
        verbose_name_plural = 'Аналитики по категориям'
        db_table = 'analytic_category_analytic'

    name = models.CharField(max_length=255)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2)
    average_receipt = models.DecimalField(max_digits=10, decimal_places=2)
