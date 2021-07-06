# Generated by Django 3.2.4 on 2021-06-29 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0016_remove_nursery_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nursery2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=255, verbose_name='English')),
                ('spanish', models.CharField(max_length=255, verbose_name='Spanish')),
                ('vietnamese', models.CharField(max_length=255, verbose_name='Vietnamese')),
                ('price', models.IntegerField(verbose_name='Prize')),
                ('size', models.CharField(max_length=150, verbose_name='size')),
                ('height', models.CharField(max_length=150, verbose_name='Height')),
            ],
        ),
        migrations.AddField(
            model_name='nursery',
            name='retail',
            field=models.IntegerField(default=0, verbose_name='Retail'),
        ),
    ]
