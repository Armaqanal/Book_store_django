from django.urls import path
from . import views

urlpatterns = [
    path('customer/<int:writer_id>/', views.a_writer_books, name='book')
]
