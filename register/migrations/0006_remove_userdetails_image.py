# Generated by Django 2.0.13 on 2019-07-25 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20190725_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='image',
        ),
    ]
