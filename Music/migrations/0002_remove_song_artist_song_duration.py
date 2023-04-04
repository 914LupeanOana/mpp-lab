# Generated by Django 4.1.7 on 2023-03-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.CharField(default='00:00', max_length=10),
            preserve_default=False,
        ),
    ]
