# Generated by Django 5.0 on 2024-07-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0004_requests_alter_stellas_options_stellas_for_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirinuky',
            name='kirinuky_stella',
            field=models.CharField(max_length=100),
        ),
    ]