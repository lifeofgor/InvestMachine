# Generated by Django 3.2.5 on 2021-08-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0023_alter_lkpage_data_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lkpage',
            name='data_page',
            field=models.DateTimeField(verbose_name='Дата'),
        ),
    ]