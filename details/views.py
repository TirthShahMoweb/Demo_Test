from django.shortcuts import render
from .models import City,Customer
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add_customer(request):
    if request.method == 'POST':
        data = json.loads(request.body)        
        customer_name = data.get('customer_name')
        customer_number = data.get('customer_number')
        customer_email = data.get('customer_email')
        customer_city = data.get('customer_city')
        customer=Customer(customer_name=customer_name,
                          customer_number=customer_number,
                          customer_email=customer_email,
                          customer_city_id=customer_city)
        customer.save()
        return HttpResponse(f"Added {data}")
    # else:
    #     return HttpResponse("Hello World")

@csrf_exempt
def edit_customer(request,customer_name):
    if request.method == 'PATCH':
        customer_data = Customer.objects.filter(customer_name=customer_name).first()
        data = json.loads(request.body)
        customer_data.customer_name = data.get('customer_name')
        customer_data.customer_number = data.get('customer_number')
        customer_data.customer_email = data.get('customer_email')
        customer_data.customer_city_id = data.get('customer_city')
        customer_data.save()
    return HttpResponse(customer_data)

@csrf_exempt
def read_customer(request):
    customer_data=Customer.objects.filter(del_customer=False).values_list()
    return HttpResponse(customer_data)

@csrf_exempt
def search(request):
    if request.method == 'GET':
        data = request.GET.get('name')
        search_data = Customer.objects.filter(customer_name__icontains=data).values_list()
        return HttpResponse(search_data)
    
def filter(request):
    if request.method == 'GET':
        data = request.GET.get('name')
        city = City.objects.filter(city_name=data).values_list().first()
        customer_data = Customer.objects.filter(customer_city=city[0])
        return HttpResponse(customer_data)      
    return HttpResponse("Hello")

def del_customer(request,customer_name):
    customer_data = Customer.objects.filter(customer_name=customer_name).first()
    customer_data.customer_del = True