# Generated by Django 3.2.5 on 2021-08-18 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_alter_modelsnewspage_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelsnewspage',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 18, 9, 33, 9, 575725), verbose_name='Дата'),
        ),
    ]
