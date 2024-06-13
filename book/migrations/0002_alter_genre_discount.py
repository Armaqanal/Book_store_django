# Generated by Django 4.2 on 2024-06-13 07:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]
