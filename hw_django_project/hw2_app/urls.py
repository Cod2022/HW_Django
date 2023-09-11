from django.urls import path 
from .views import orders, upload_image


urlpatterns = [
    path('orders/<int:client_id>/', orders, name='orders'),
    path('upload_image', upload_image, name='upload_image')
]