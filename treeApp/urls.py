from django.urls import path
from .views import *
from rest_framework.authtoken import views
    # URLConfiguration
    # Take a lock at example.json
urlpatterns = [
    path('register/', registration , name="register"),
    path('login/', views.obtain_auth_token, name='login'),

    path('orders/', workOrder.as_view()),
    path('clients/', client.as_view()),
    path('requirements/', requirements_view.as_view()),
    path('deleteitem/<int:pk>/', delete_item, name="deleteOrder"),
    path('deleteRequirement/<int:pk>/', delete_requirment_item, name="deleteRequirement"),
    path('updateItem/<int:pk>/', update_item, name="updateOrder"),
    path('updateRequiredItem/<int:pk>/', update_requirment_item , name="updateRequirment"),
    path('clientPhone/', check_clientPhone, name="clientPhone"),
    path('getUnfinishedOrders/', get_unfinishedOrders, name="getUnfinishedOrders"),
    path('searchByDate/', search_byDate, name="searchByDate"),
    path('searchByOrderId/', search_ByOrderId, name="searchByOrderId"),

]
