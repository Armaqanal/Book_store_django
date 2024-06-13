# Generated by Django 4.2 on 2024-06-13 07:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('published_at', models.DateField()),
                ('age_limit', models.IntegerField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(120)])),
                ('genre', models.ManyToManyField(to='book.genre')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book.publisher')),
            ],
        ),
    ]
