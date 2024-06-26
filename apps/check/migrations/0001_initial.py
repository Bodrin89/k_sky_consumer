# Generated by Django 5.0.4 on 2024-04-16 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nds_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tips_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=255)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmodel')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.storemodel')),
            ],
            options={
                'verbose_name': 'Проверка',
                'verbose_name_plural': 'Проверки',
                'db_table': 'check_check',
            },
        ),
    ]
