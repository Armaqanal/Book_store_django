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
