from django.shortcuts import render
from .models import Book
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
