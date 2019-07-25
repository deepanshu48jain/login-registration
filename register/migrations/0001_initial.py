# Generated by Django 2.0.13 on 2019-07-25 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=50)),
                ('mobile_no', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
