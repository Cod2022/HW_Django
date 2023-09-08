from django.shortcuts import render, get_object_or_404
from .models import Client, Product, Order

def orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client)
    context = {'client': client, 'orders': orders}
    return render(request, 'hw2_app/orders.html', context)
    


