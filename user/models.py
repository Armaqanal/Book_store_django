from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from book.models import Book


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)  # TODO:INHERITANCE

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Customer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    age = models.IntegerField(validators=[
        MinValueValidator(5),
        MaxValueValidator(120)
    ])
    user_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.user_name}'


class Writer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    email = models.EmailField()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        ordering = [
            'email'
        ]
