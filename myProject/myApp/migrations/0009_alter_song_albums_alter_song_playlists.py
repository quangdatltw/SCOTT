# Generated by Django 5.0.4 on 2024-04-23 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_song_artists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='albums',
            field=models.ManyToManyField(blank=True, related_name='songs', to='myApp.album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='playlists',
            field=models.ManyToManyField(blank=True, related_name='songs', to='myApp.playlist'),
        ),
    ]
