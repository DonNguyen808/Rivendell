# Generated by Django 3.2.4 on 2021-06-26 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_search_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nursery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=255, verbose_name='English')),
                ('spanish', models.CharField(max_length=255, verbose_name='Spanish')),
                ('vietnamese', models.CharField(max_length=255, verbose_name='Vietnamese')),
                ('retail', models.IntegerField(verbose_name='Retail')),
                ('size', models.CharField(max_length=150, verbose_name='size')),
                ('height', models.CharField(max_length=150, verbose_name='Height')),
            ],
        ),
    ]
