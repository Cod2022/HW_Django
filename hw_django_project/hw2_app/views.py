from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage 
from .models import Client, Product, Order
from .forms import ProductImageForm

def orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    # orders = Order.objects.filter(customer=client)
    orders = Order.objects.filter(customer=client).prefetch_related('products')
    products = [product for order in orders for product in order.products.all()]
    context = {'client': client, 'orders': orders, 'products': products}
    return render(request, 'hw2_app/orders.html', context)

def upload_image(request):
    message = 'Ошибка загрузки'
    if request.method == 'POST': 
        form = ProductImageForm(request.POST, request.FILES) 
        if form.is_valid(): 
            image = form.cleaned_data['image'] 
            fs = FileSystemStorage()
            fs.save(image.name, image)
            message = 'Фото успешно загружено' 
    else: 
        form = ProductImageForm() 
        message = 'Загрузите фото продукта'
    return render(request, 'hw2_app/upload_image.html', {'form': form, 'message': message})
    


