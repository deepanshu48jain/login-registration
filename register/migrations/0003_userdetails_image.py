# Generated by Django 2.0.13 on 2019-07-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_remove_userdetails_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='image',
            field=models.FileField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]