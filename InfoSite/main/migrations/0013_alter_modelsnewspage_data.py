# Generated by Django 3.2.5 on 2021-07-23 00:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_modelsnewspage_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelsnewspage',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 23, 3, 7, 35, 307841), verbose_name='Дата'),
        ),
    ]
