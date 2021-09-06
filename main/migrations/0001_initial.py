# Generated by Django 2.2.7 on 2019-12-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=200)),
                ('drive_unit', models.CharField(max_length=200)),
                ('engine_volume', models.FloatField(max_length=10)),
            ],
        ),
    ]
