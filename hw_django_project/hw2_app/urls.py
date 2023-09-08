from django.urls import path 
from .views import orders


urlpatterns = [
    path('orders/<int:client_id>/', orders, name='orders'),
]