from django.urls import path
from .views import *
from rest_framework.authtoken import views
    # URLConfiguration
urlpatterns = [
    path('register', registration , name="register"),
    path('login/', views.obtain_auth_token, name='login'),

    path('orders/', workOrder.as_view()),
    path('clients/', client.as_view()),
    path('deleteitem/<int:pk>/', delete_item, name="deleteOrder"),
    path('updateItem/<int:pk>/', update_item, name="updateOrder"),
    path('clientPhone/', check_clientPhone, name="clientPhone"),


]