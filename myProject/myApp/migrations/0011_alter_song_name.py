# Generated by Django 5.0.4 on 2024-05-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_rename_like_count_song_view_count_song_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]