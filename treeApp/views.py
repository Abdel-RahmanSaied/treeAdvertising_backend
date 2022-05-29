from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import client_serializers
from .serializers import  orders_serializers, client_serializers

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

import json

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

@api_view(['DELETE',])
def delete_item(request, pk):
      if request.method == 'DELETE':
            item=orders.objects.filter(order_id=pk)
            item.delete()
            return Response()

@api_view(['PUT',])
def update_item(request,pk):
    json_response = json.load(request)
    print(json_response)
    obj_list = ["recived_date","delivery_date","design_types","design_path","design_category","printing_type","size_width","size_high","materials","color",
                "thickness","Post_print_services","state"]

    for object in obj_list :
        print(object)
        if object in json_response:
            #doctor_requested_id = json_response[object]
            verified_object = orders.objects.filter(order_id=pk)
            verified_object.update(**json_response)
    return Response()