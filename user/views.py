from django.shortcuts import render
from . import models
from book.models import Book


# Create your views here.
def all_customers(request):
    customers = models.Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customer.html', context)


def a_customer_books(request, customer_id):
    # way1  :related_name
    customer = models.Customer.objects.get(id=customer_id)
    u_orders = customer.order_set.all()
    books = Book.objects.filter(order__in=u_orders)

    # way 2:No need customer_object
    Book.objects.filter(order__customer__pk=customer_id)


def most_popular_writer(request):
    all_writers = models.Writer.objects.all()
    popular_writer = {"writer": None, "max_quantity": 0}
    for writer in all_writers:
        all_books = writer.books.all()
        total_quantity = 0
        for book in all_books:
            orders_book = book.order_set.all()
            total_quantity += sum([order.quantity for order in orders_book])
        if total_quantity > popular_writer["max_quantity"]:
            popular_writer["max_quantity"] = total_quantity
            popular_writer["writer"] = writer
    return render(request, 'writer.html', popular_writer)
