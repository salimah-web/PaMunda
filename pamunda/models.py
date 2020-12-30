from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    images=models.ImageField(null=True,blank=True,upload_to="images/")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')


class Product(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=50, default='others')
    Product_name= models.CharField(max_length=100)
    measurement_scale= models.CharField(max_length=100)
    price_per_Scale= models.DecimalField(max_digits=10, decimal_places=2)
    Quantity_available= models.IntegerField()
    location=models.CharField(max_length=50, default='Kano')
    phone_number=models.CharField(max_length=15,default='01-6547-5674')
    image=models.ImageField(null=True,blank=True,upload_to="images/")

    def __str__(self):
        return self.Product_name

    def get_absolute_url(self):
        return reverse('homepage')


class Make_order(models.Model):
    Quantity= models.DecimalField(max_digits=10, decimal_places=2)
    Location = models.CharField(max_length=20)
    def __str__(self):
        return self.Quantity

class user_profile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    location=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=15)
    bio=models.TextField(max_length=200)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('homepage')
