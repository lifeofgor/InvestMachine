# Generated by Django 3.2.5 on 2021-08-18 06:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0025_alter_lkpage_data_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lkpage',
            name='data_page',
        ),
        migrations.AddField(
            model_name='lkpage',
            name='created_page',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lkpage',
            name='updated_page',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
