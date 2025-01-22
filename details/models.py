from django.db import models

# Create your models here.


class City(models.Model):
    city_name=models.CharField(max_length=55,unique=True)

class Customer(models.Model):
    customer_name=models.CharField(max_length=50, unique=True)
    customer_number=models.IntegerField()
    customer_email=models.CharField(max_length=25)
    customer_city=models.ForeignKey(City,on_delete=models.CASCADE)
    customer_del = models.BooleanField(default=False)