# Generated by Django 4.0.4 on 2022-06-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_orders_order_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='total_price',
            field=models.IntegerField(blank=True, default=0, verbose_name='Конечная стоимость товаров'),
            preserve_default=False,
        ),
    ]