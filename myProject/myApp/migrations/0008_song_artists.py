# Generated by Django 5.0.4 on 2024-04-23 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_alter_song_albums_alter_song_playlists'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artists',
            field=models.ManyToManyField(related_name='songs', to='myApp.artist'),
        ),
    ]
