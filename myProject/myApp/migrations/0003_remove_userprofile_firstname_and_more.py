# Generated by Django 5.0.4 on 2024-04-19 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_alter_playlist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='lastname',
        ),
    ]
