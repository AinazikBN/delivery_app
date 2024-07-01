# Generated by Django 5.0.6 on 2024-06-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='stock',
            field=models.CharField(choices=[('in_stock', 'Доступен к заказу'), ('out_stock', 'Стоп-лист')], max_length=50, null=True),
        ),
    ]