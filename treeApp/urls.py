from django.urls import path
from .views import *
    # URLConfiguration
urlpatterns = [
    path('orders', workOrder.as_view()),
    path('clients', client.as_view()),
    path('deleteitem/<int:pk>/', delete_item, name="deleteOrder"),
    path('updateItem/<int:pk>/', update_item, name="updateOrder"),
]