# Generated by Django 3.2.5 on 2021-08-04 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0009_auto_20210731_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='lkpage',
            name='data_page',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 4, 15, 36, 42, 923450), verbose_name='Дата'),
        ),
    ]