# Generated by Django 5.0 on 2024-01-09 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kirinuky',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kirinuky_stella', models.CharField(max_length=30)),
                ('kirinuky_link', models.CharField(max_length=300)),
                ('kirinuky_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stellas',
            fields=[
                ('stella_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replay_link', models.CharField(max_length=300)),
                ('replay_day', models.DateField()),
                ('replay_contents', models.CharField(max_length=100)),
                ('stella', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mains.stellas')),
            ],
        ),
    ]
