# Generated by Django 5.0.6 on 2024-07-01 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_price_menu_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='stock',
            field=models.CharField(choices=[('in_stock', 'Доступен к заказу'), ('out_stock', 'Стоп-лист')], max_length=50),
        ),
    ]
