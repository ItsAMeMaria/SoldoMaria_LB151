# Generated by Django 4.1.5 on 2023-02-25 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gluecksrad', '0008_alter_word_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gluecksrad.category'),
        ),
    ]
