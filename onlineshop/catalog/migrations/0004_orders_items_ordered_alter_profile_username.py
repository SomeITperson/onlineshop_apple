# Generated by Django 4.0.4 on 2022-06-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='items_ordered',
            field=models.CharField(blank=True, max_length=200, verbose_name='id`s товаров'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=20, verbose_name='Имя(id заказчика)'),
        ),
    ]
