# Generated by Django 4.1.5 on 2023-02-25 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gluecksrad', '0005_word'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='word',
            old_name='word',
            new_name='word_text',
        ),
        migrations.AlterField(
            model_name='word',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gluecksrad.category'),
        ),
    ]
