from django.db import models
from book.models import Book
from user.models import Customer


# Create your models here.
class Order(models.Model):
    quantity = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # sale_price = models.DecimalField(max_digits=3, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def calculate_sale_price(self):
        return self.book.price * self.quantity  # TODO: VIEW

    def __str__(self):
        return f" {self.book}-{self.quantity}"
