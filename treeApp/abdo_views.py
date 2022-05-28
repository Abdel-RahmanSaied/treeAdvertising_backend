from dataclasses import field
#from tkinter.messagebox import YES
#from turtle import color
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated
from django.db.models import Q

@api_view(['GET','POST'])
def list_order(request):
   if request.method == "GET":
      orders=Order.objects.all()
      serializer=Orderserilaizer(orders,many=True)
      return Response(serializer.data)
   elif request.method == "POST":
      serializer=Orderserilaizer(data=request.data)
      if  serializer.is_valid():
         serializer.save()
         return Response(serializer.data)

@api_view(['POST'])
def signup(request):
   name=request.data["name"]
   username=request.data["username"]
   email=request.data["email"]
   age=request.data["age"]
   gender=request.data["gender"]
   prefercolor=request.data["prefercolor"]
   preferstyle=request.data["preferstyle"]
   password1=request.data["password1"]
   password2=request.data["password2"]
   if password1==password2:
      user=User.objects.create_user(username=username,password=password1)
      user.save()
      customer=Customer.objects.create(user=user,name=name,email=email,age=age,gender=gender, prefercolor= prefercolor,preferstyle=preferstyle)
      customer.save()
      token=Token.objects.create(user=user)
      token.save()
   return Response(request.data)


class addProduct(generics.ListCreateAPIView):
      permission_classes = (permissions.IsAuthenticated,)
      queryset = Product.objects.filter(filter=True)
      serializer_class = Productserilaizer

@permission_classes((IsAuthenticated,))
@api_view(['DELETE',])
def delete_item(request, pk):
      if request.method == 'DELETE':
            item=Product.objects.filter(id=pk)
            item.delete()
            return Response()


@api_view(['PUT'])
def hide_item(request,id):
      if request.method =='POST':
            item=Product.objects.get(id=id)
            item.field =False
            item.save()

@api_view(['POST'])
def search(request):
    query = request.data.get('name', '')
    if query:
        products = Product.objects.filter(Q(name=query))
        serializer = Productserilaizer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})

@api_view(['POST'])
def filter(request):
    name1 = request.data.get('name', '')
    size1 = request.data.get('size', '')
    color1 = request.data.get('color', '')
    style1 = request.data.get('style', '')
    try:
        products = Product.objects.filter(Q(name=name1) and Q(style=style1) and Q(color=color1) and Q(available_sizes=size1)
            or Q(name=name1) and Q(style=style1) and Q(color=color1)
            or Q(name=name1) and Q(style=style1) and Q(available_sizes=size1)
            or Q(name=name1) and Q(color=color1) and Q(available_sizes=size1)
            or Q(style=style1) and Q(color=color1) and Q(available_sizes=size1)
            or Q(name=name1) and Q(style=style1)
            or Q(name=name1) and Q(color=color1)
            or Q(name=name1) and Q(available_sizes=size1)
            or Q(style=style1) and Q(color=color1)
            or Q(style=style1) and Q(available_sizes=size1)
            or Q(color=color1) and Q(available_sizes=size1)
            or Q(name=name1)
            or Q(style=style1)
            or Q(color=color1)
            or Q(available_sizes=size1) )
        serializer = Productserilaizer(products, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response({"products": []})



class order_info(generics.ListCreateAPIView):
      permission_classes = (permissions.IsAuthenticated,)
      queryset = Order.objects.all()
      serializer_class = Orderserilaizer


class categoryDitail(generics.RetrieveUpdateDestroyAPIView):
      permission_classes = (permissions.IsAuthenticated,)
      queryset = Category.objects.all()
      serializer_class = Categoryserilaizer

class styleDitail(generics.RetrieveUpdateDestroyAPIView):
      permission_classes = (permissions.IsAuthenticated,)
      queryset = Style.objects.all()
      serializer_class = Styleserilaizer

class branchDitail(generics.RetrieveUpdateDestroyAPIView):
      permission_classes = (permissions.IsAuthenticated,)
      queryset = Branch.objects.all()
      serializer_class = Branchserilaizer

class colorDitail(generics.RetrieveUpdateDestroyAPIView):
      permission_classes = (permissions.IsAuthenticated,)
      queryset = Color.objects.all()
      serializer_class = Colorserilaizer
#########################################################################
#Body_Mesurment
# class body_mesurment(generics.RetrieveUpdateDestroyAPIView):
#       permission_classes = (permissions.IsAuthenticated,)
#       queryset = Body_Mesurment.objects.all()
#       serializer_class = Body_mesurmentserilaizer

