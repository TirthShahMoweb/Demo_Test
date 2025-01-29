from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import City,Customer



@csrf_exempt
def add_customer(request):
    '''
        This method is for adding new customer.
    '''
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        number = data.get('number')
        email = data.get('email')
        city = data.get('city')
        customer=Customer(name = name,
                          number = number,
                          email = email,
                          city_id = city)
        customer.save()
        return HttpResponse(f"{name} has been added.")
    return HttpResponse("Add Data")

@csrf_exempt
def edit_customer(request, name: str):
    '''
        This method is for editing customer.
    '''
    if request.method == 'PATCH':
        customer_data = Customer.objects.filter(name=name).first()
        data = json.loads(request.body)
        customer_data.name = data.get('name')
        customer_data.number = data.get('number')
        customer_data.email = data.get('email')
        customer_data.city_id = data.get('city')
        customer_data.save()
    return HttpResponse(customer_data)

def read_customer(request):
    '''
        This method is for reading customer data.
    '''
    customer_data = Customer.objects.filter(is_deleted=False).values_list()
    return HttpResponse(customer_data)

def search(request):
    '''
        This method is for searching on the basis of customer name.
    '''
    if request.method == 'GET':
        data = request.GET.get('name')
        search_data = Customer.objects.filter(name__contains=data).values_list()
        return HttpResponse(search_data)

def filter(request):
    '''
        This method is for filtering customer on the basis of their respective cities.
    '''
    if request.method == 'GET':
        data = request.GET.get('name')
        city = City.objects.filter(name=data).values_list().first()
        customer_data = Customer.objects.filter(city=city[0])
        return HttpResponse(customer_data)
    return HttpResponse("Please use proper Method")

def del_customer(request,name: str):
    '''
        This method is for deleting customer.
    '''
    customer_data = Customer.objects.filter(name=name).first()
    customer_data.is_deleted = True
    customer_data.save()
    return HttpResponse("Customer has been deleted Successfully.")