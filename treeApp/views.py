from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import client_serializers
from .serializers import  orders_serializers, client_serializers, users_serializers

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

import json

# Create your views here.

class workOrder(APIView):
    permission_classes = []
    def __init__(self):
        pass
    def get(self, request):
        orderList = orders.objects.all()
        serializer = orders_serializers(orderList, many=True)
        return Response(serializer.data)
    def post(self , request):
        user_id = self.request.data["user_id"]
        client_id = self.request.data["client_id"]
        recived_date = self.request.data["recived_date"]
        delivery_date = self.request.data["delivery_date"]
        design_types = self.request.data["design_types"]
        design_path= self.request.data["design_path"]
        design_category= self.request.data["design_category"]
        printing_type= self.request.data["printing_type"]
        size_width=  self.request.data["size_width"]
        size_high=float( self.request.data["size_high"])
        materials= self.request.data["materials"]
        color= self.request.data["color"]
        thickness= self.request.data["thickness"]
        Post_print_services= self.request.data["Post_print_services"]
        state= self.request.data["state"]
        notes= self.request.data["notes"]

        serializer = orders_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response("failed", status=401)

class client(APIView):
    permission_classes = []
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

@api_view(['POST', ])
@permission_classes([])
def registration(request):
    username = request.data["username"]
    department = request.data["department"]
    password1 = request.data["password1"]
    password2 = request.data["password2"]
    serializer = users_serializers(data=request.data)
    if serializer.is_valid() and password1 == password2:
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        nuser = Users.objects.create(user=user, name=username, department=department )
        token = Token.objects.get(user=user).key
        nuser.save()
        data = request.data
        data.update({'token':token})
        return Response(data)
    else:
        return Response('password must match.', status=401)


### Example ###
#Register# {  "name": "mohamed", "username": "mok11", "department": "M","password1": "123", "password2": "123" }
#login# { "username":"mok11", "password":"123"}
# 'Authorization' : 'Token 70dbe36a87dfe681f98e6a8870150138e7bd4aa3'

# @api_view(['POST', ])
# def registration(request):
#     if request.method == 'POST':
#         department = request.data["department"]
#         serializer = users_serializers(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             account = serializer.save()
#             nuser = Users.objects.create(user=account, name=account.username, department=department)
#             nuser.save()
#             data['response'] = "successfully registered a new user."
#             data['name'] = account.username
#             data['department'] = account.department
#             token = Token.objects.get(user=account).key
#             data['token'] = token
#         else:
#             data = serializer.errors
#         return Response(data)


@api_view(['POST', ])
def check_clientPhone(request):
    if request.method == 'POST':
        client_phone = request.data["phone"]
        if clients.objects.filter(phone_number=client_phone).exists():
            return Response(True, status=200)
        else:
            return Response("Not exist", status=404)


@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def delete_item(request, pk):
    user_instance = Users.objects.get(user=request.user)
    if user_instance.department == 'M':
        if request.method == 'DELETE':
            item=orders.objects.filter(order_id=pk)
            item.delete()
            return Response()
    else:
        return Response({'Response':"You don't have permission to delete this."})


@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def update_item(request,pk):

    json_response = json.load(request)
    # print(json_response)
    obj_list = ["recived_date","delivery_date","design_types","design_path","design_category","printing_type","size_width","size_high","materials","color",
                "thickness","Post_print_services","state"]

    for object in obj_list:
        # print(object)
        if object in json_response:
            #doctor_requested_id = json_response[object]
            verified_object = orders.objects.filter(order_id=pk)
            verified_object.update(**json_response)
    return Response()

