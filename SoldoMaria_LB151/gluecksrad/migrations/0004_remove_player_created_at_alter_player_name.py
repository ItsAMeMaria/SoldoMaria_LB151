# Generated by Django 4.1.5 on 2023-02-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gluecksrad', '0003_rename_playername_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]