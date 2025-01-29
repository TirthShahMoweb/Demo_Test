from django.urls import path
from . import views

urlpatterns = [
    # CRUD operation of customer.
    path('add_customer/', views.add_customer, name='add_customer'),
    path('delete/<str:name>/', views.del_customer, name='del_customer'),
    path('edit_customer/<str:name>/', views.edit_customer, name='edit_customer'),
    path('read_customer/', views.read_customer, name='read'),

    # Search and filter.
    path('filter', views.filter, name='filter'),
    path('search', views.search, name='search')
    ]