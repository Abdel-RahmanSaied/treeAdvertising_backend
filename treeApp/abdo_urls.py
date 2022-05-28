from unicodedata import name
from django.urls import path,include
from .views import *

urlpatterns = [
    path('list_orders/',list_order,name='list_order'),
    path('signup/',signup),
    path('products/search/', search,name="search"),
    path('addProduct/',addProduct.as_view(),name="addproduct"),
    path('filter/',filter,name="filter"),
    path('order_info/',order_info.as_view(),name="order_info"),
    path('colorditail/<int:pk>/',colorDitail.as_view(),name="colorditail"),
    path('deleteitem/<int:pk>/',delete_item,name="deleteProduct"),
    path('styleditail/<int:pk>/',styleDitail.as_view(),name="styleditail"),
    path('branchditail/<int:pk>/',branchDitail.as_view(),name="branchditail"),
    path('categoryditail/<int:pk>/',categoryDitail.as_view(),name="categoryditail"),
#   path('bodymesurment/',Body_Mesurment.as_view(),name="bodyesurment"),
]

# {
# "username":"finaltest",
# "password1":"123456789",
# "password2":"123456789",
# "email":"final@gmail.com",
# }