# Generated by Django 3.2.5 on 2021-08-06 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_comment_lkpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
