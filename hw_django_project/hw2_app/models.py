# ДЗ 4:
# Измените модель продукта, добавьте поле для хранения фотографии продукта.
# Создайте форму, которая позволит сохранять фото.



from django.db import models
from datetime import datetime

class Client(models.Model): 
    name = models.CharField(max_length=100) 
    email = models.EmailField() 
    phone_number = models.IntegerField()
    adress = models.TextField()
    registration_date = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'Client: {self.name}, email: {self.email}, phone_number: {self.phone_number},\
                 adress: {self.adress}, registration_date: {self.registration_date}'
    

class Product(models.Model): 
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2) 
    product_amount = models.IntegerField()
    date = models.DateTimeField(default = datetime.now())
    image = models.ImageField()


class Order(models.Model): 
    customer = models.ForeignKey(Client, on_delete=models.CASCADE) 
    products = models.ManyToManyField(Product) 
    date_ordered = models.DateTimeField(default = datetime.now()) 
    total_price = models.DecimalField(max_digits=8, decimal_places=2)



