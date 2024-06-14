from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_customers, name='user'),
    path('<int:customer_id>/', views.a_customer_books, name='customer-books'),
    path('most/', views.most_popular_writer, name='most')
]
