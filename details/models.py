from django.db import models



class City(models.Model):
    name = models.CharField(max_length=55,unique=True)

class Customer(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(null=True, unique=True)
    email = models.CharField(max_length=25)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)