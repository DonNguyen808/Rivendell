# Generated by Django 3.2.4 on 2021-06-29 04:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_alter_nursery_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nursery',
            name='retail',
        ),
        migrations.AddField(
            model_name='nursery',
            name='price',
            field=models.IntegerField(default=django.utils.timezone.now, verbose_name='Price'),
            preserve_default=False,
        ),
    ]