# Generated by Django 3.2.4 on 2021-06-29 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_remove_nursery_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='nursery',
            name='price',
            field=models.IntegerField(default=int, verbose_name='Price'),
            preserve_default=False,
        ),
    ]