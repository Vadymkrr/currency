# Generated by Django 4.1.6 on 2023-02-26 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0005_source_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='source',
            old_name='surname',
            new_name='source_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='age',
        ),
        migrations.RemoveField(
            model_name='source',
            name='city',
        ),
    ]