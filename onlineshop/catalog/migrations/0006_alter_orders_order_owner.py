# Generated by Django 4.0.4 on 2022-06-14 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_orders_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.profile', verbose_name='Заказчик(id)'),
        ),
    ]
