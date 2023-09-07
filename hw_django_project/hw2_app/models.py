# ДЗ 2:
# Создайте три модели Django: клиент, товар и заказ.

# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара

# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказаa

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


class Order(models.Model): 
    customer = models.ForeignKey(Client, on_delete=models.CASCADE) 
    products = models.ManyToManyField(Product) 
    date_ordered = models.DateTimeField(default = datetime.now()) 
    total_price = models.DecimalField(max_digits=8, decimal_places=2)



