from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import clients, orders
from .serializers import client_serializers
from .serializers import  orders_serializers, client_serializers

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.

class workOrder(APIView):
    def __init__(self):
        pass
    def get(self, request):
        orderList = orders.objects.all()
        serializer = orders_serializers(orderList, many=True)
        return Response(serializer.data)
    def post(self , request):
        user_name = self.request.data["user_id"]
        client_name = self.request.data["client_id"]
        recived_date = self.request.data["recived_date"]
        delivery_date = self.request.data["delivery_date"]
        design_types = self.request.data["design_types"]
        design_path= self.request.data["design_path"]
        design_category= self.request.data["design_category"]
        printing_type= self.request.data["printing_type"]
        size_width= self.request.data["size_width"]
        size_high= self.request.data["size_high"]
        materials= self.request.data["materials"]
        color= self.request.data["color"]
        thickness= self.request.data["thickness"]
        Post_print_services= self.request.data["Post_print_services"]
        state= self.request.data["state"]

        serializer = orders(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.data , status=404)


class client(APIView):
    def __int__(self):
        pass
    def get(self, request):
        client_list = clients.objects.all()
        serializer = client_serializers(client_list, many=True)
        return Response(serializer.data)
    def post(self, request):
        client_name = self.request.data["name"]
        client_phone = self.request.data["phone_number"]
        client_level = self.request.data["clientlevel"]

        serializer = client_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.data , status=404)