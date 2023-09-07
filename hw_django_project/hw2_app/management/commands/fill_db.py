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
            for j in range (1, 6):
                product = Product(name=f'name_{j}', description=f'description_{j}', price= j * 3, product_amount= j, 
                                  date= datetime.datetime(2022, 3, 11))
                product.save()
                for k in range (1, 6): 
                    order = Order(customer = client, products = product, date_ordered=datetime.datetime(2023, random.randint(1, 12), random.randint(1, 30)))
                    order.save()
