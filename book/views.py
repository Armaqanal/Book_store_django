from django.shortcuts import render
from .models import Book, Genre
from user.models import Writer


# Create your views here.
def a_writer_books(request, writer_id):
    # way 1
    w = Writer.objects.get(id=writer_id)
    books = w.books.all()

    # way 2-1
    # Book.objects.filter(writer=w)

    # way 3
    # Book.objects.filter(writer__pk=1)
    # Book.objects.filter(writer=1)


# Question4
def a_publisher_books(request, publisher_id):
    # access through Book way 1
    Book.objects.filter(publisher=publisher_id)

    # access through publisher way 2
    # p1 = Publisher.objects.filter(id=publisher_id)[0]

    # p2 = Publisher.objects.get(id=1)


# Question 5
def genre_books(request, genre_id):
    g = Genre.objects.get(id=genre_id)
    g.book_set.all()


# question 6

# show the first max book
# from django.db.models import Sum

# Book.objects.all().annotate(sum_orders=Sum(order__quantity))
# books.first().sum_orders
# from django.db.models import Max
#
# books.aggregate(max=Max("sum_orders"))
# books.order_by("-sum_orders").first()

# show max books
#  max=books.aggregate(max=Max("sum_orders")).get("max")
# books.filter(sum_orders=max)

# Done for test
#  books.values("title","sum_orders")


