# Generated by Django 3.2.4 on 2021-06-29 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0013_nursery_retail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nursery',
            name='retail',
        ),
    ]