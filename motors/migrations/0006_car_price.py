# Generated by Django 4.2.1 on 2023-07-20 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0005_car_batareya_quvvati_en_car_batareya_quvvati_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]