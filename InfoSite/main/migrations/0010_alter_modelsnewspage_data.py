# Generated by Django 3.2.5 on 2021-07-21 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_modelsnewspage_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelsnewspage',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 21, 18, 19, 5, 450149), verbose_name='Дата'),
        ),
    ]
