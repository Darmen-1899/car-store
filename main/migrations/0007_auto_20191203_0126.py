# Generated by Django 2.2.7 on 2019-12-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_car_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='acceleration',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='car',
            name='power',
            field=models.CharField(default='', max_length=15),
        ),
    ]
