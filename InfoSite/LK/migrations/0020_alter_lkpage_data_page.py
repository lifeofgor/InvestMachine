# Generated by Django 3.2.5 on 2021-08-17 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0019_alter_lkpage_data_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lkpage',
            name='data_page',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 17, 16, 38, 38, 855236), verbose_name='Дата'),
        ),
    ]
