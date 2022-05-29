from django.urls import path
from . import views
    # URLConfiguration
urlpatterns = [
    path('orders', views.workOrder.as_view()),
    path('clients', views.client.as_view()),
    ]