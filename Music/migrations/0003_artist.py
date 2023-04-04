# Generated by Django 4.1.7 on 2023-03-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0002_remove_song_artist_song_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CNP', models.CharField(max_length=14, unique=True)),
                ('artist_name', models.CharField(max_length=100)),
                ('real_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
