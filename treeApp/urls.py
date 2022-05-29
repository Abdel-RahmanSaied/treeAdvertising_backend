from django.urls import path
from . import views
    # URLConfiguration
urlpatterns = [
    path('api/', views.workOrder.as_view() , name = "orders")
    ]