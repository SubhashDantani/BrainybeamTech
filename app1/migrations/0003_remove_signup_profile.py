# Generated by Django 3.1.8 on 2022-06-27 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20220627_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='profile',
        ),
    ]
