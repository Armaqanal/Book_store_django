from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=3, decimal_places=2,
                                   validators=[MinValueValidator(0.00), MaxValueValidator(1.00)], default=0.00,
                                   null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2,
                                   validators=[MinValueValidator(0.00), MaxValueValidator(1.00)], null=True, blank=True)
    published_at = models.DateField()
    genre = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    age_limit = models.IntegerField(validators=[
        MinValueValidator(5),
        MaxValueValidator(120)
    ])

    def __str__(self):
        return self.title
