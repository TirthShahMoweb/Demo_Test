from django.urls import path
from . import views

urlpatterns = [
    path('add_customer/',views.add_customer, name='add_customer'),
    path('edit_customer/<str:customer_name>/',views.edit_customer, name='edit_customer'),
    path('search',views.search,name='search'),
    path('filter',views.filter,name='filter'),
    path('read_customer/',views.read_customer,name='read')
    ]