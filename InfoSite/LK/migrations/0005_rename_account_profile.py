# Generated by Django 3.2.5 on 2021-07-23 00:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LK', '0004_auto_20210722_0140'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='Profile',
        ),
    ]