# Generated by Django 3.2.5 on 2021-08-06 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_modelsnewspage_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelsnewspage',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 6, 5, 15, 17, 307643), verbose_name='Дата'),
        ),
    ]
