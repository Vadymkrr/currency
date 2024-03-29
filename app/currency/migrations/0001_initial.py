# Generated by Django 4.1.6 on 2023-04-06 10:53

import currency.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('request_method', models.CharField(max_length=255)),
                ('time', models.FloatField()),
            ],
            options={
                'verbose_name': 'Request, Response, Log',
                'verbose_name_plural': 'Request, Response, Log',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=64)),
                ('avatar', models.FileField(
                    blank=True,
                    default=None,
                    null=True,
                    upload_to=currency.models.avatar_path)),
                ('code_name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('currency', models.PositiveSmallIntegerField(
                    choices=[(1, 'Dollar'), (2, 'Euro'), (3, 'Hryvnia')],
                    default=1)),
                ('buy', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sale', models.DecimalField(decimal_places=2, max_digits=6)),
                ('source', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='rates',
                    to='currency.source')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
