from django.core.management.base import BaseCommand 
from hw2_app.models import Client, Product, Order
import datetime
import random

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for i in range (1, 6):
            client = Client(name=f'Name_{i}', email=f'mail{i}@mail.ru', phone_number=8906567 + i, adress=f'adress_{i}',
                            registration_date= datetime.datetime(2022, 3, 11))
            client.save()
            orders = Order.objects.create(customer=client, total_price=120)
            for j in range (1, 6):
                product = Product(name=f'name_{j}', description=f'description_{j}', price= j * 3, product_amount= j, 
                                  date= datetime.datetime(2022, 3, 11))
                product.save()
                orders.products.add(product)
