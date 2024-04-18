from django.db import models

from apps.check.models import CheckModel


class CategoryModel(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'product_category'

    name = models.CharField(verbose_name='Название', max_length=255)


class ProductModel(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'product_product'

    product_id = models.PositiveIntegerField(unique=True, verbose_name='ID Товара')
    quantity = models.PositiveIntegerField(verbose_name='Количество в чеке')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(
        CategoryModel, on_delete=models.CASCADE, verbose_name='Категория', related_name='products'
    )
    check_transaction = models.ForeignKey(
        CheckModel, on_delete=models.CASCADE, verbose_name='Чек', related_name='items'
    )
