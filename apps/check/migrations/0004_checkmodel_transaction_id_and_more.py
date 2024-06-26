# Generated by Django 5.0.4 on 2024-04-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0003_alter_checkmodel_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkmodel',
            name='transaction_id',
            field=models.PositiveIntegerField(default=1, unique=True, verbose_name='ID транзакции'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkmodel',
            name='nds_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='сумма НДС'),
        ),
        migrations.AlterField(
            model_name='checkmodel',
            name='payment_method',
            field=models.CharField(max_length=255, verbose_name='способ оплаты'),
        ),
        migrations.AlterField(
            model_name='checkmodel',
            name='timestamp',
            field=models.DateTimeField(verbose_name='время совершения покупки'),
        ),
        migrations.AlterField(
            model_name='checkmodel',
            name='tips_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='сумма чаевых'),
        ),
        migrations.AlterField(
            model_name='checkmodel',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='общая сумма чека'),
        ),
    ]
