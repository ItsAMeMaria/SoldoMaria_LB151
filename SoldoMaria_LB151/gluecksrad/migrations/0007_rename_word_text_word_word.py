# Generated by Django 4.1.5 on 2023-02-25 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gluecksrad', '0006_category_rename_word_word_word_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='word_text',
            new_name='word',
        ),
    ]
