# Generated by Django 3.2.5 on 2021-08-06 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0012_alter_lkpage_data_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lkpage',
            name='data_page',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 6, 5, 15, 17, 305644), verbose_name='Дата'),
        ),
    ]
