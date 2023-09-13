# ДЗ 5:
# Настройте под свои нужды вывод информации о клиентах, 
# товарах и заказах на страницах вывода информации об объекте и вывода списка объектов.

from django.contrib import admin
from .models import Client, Product, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'registration_date']
    ordering = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'product_amount', 'date']
    ordering = ['date']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered']
    ordering = ['date_ordered']

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)



