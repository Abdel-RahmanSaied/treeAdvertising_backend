from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models import Q
import json

# Create your views here.

class workOrder(APIView):
    # permission_classes = []
    def __init__(self):
        pass
    def get(self, request):
        orderList = orders.objects.all()
        serializer = orders_serializers(orderList, many=True)
        return Response(serializer.data)
    def post(self , request):
        user_instance = Users.objects.get(user=request.user)
        user_id = user_instance.id
        self.request.data["user_id"] = user_id
        # user_id = self.request.data["user_id"]
        client_id = self.request.data["client_id"]
        recived_date = self.request.data["recived_date"]
        delivery_date = self.request.data["delivery_date"]
        design_types = self.request.data["design_types"]
        design_path = self.request.data["design_path"]
        design_category = self.request.data["design_category"]
        printing_type = self.request.data["printing_type"]
        size_width = self.request.data["size_width"]
        size_high = self.request.data["size_high"]
        materials = self.request.data["materials"]
        color = self.request.data["color"]
        thickness = self.request.data["thickness"]
        Post_print_services = self.request.data["Post_print_services"]
        state = self.request.data["state"]
        notes = self.request.data["notes"]

        serializer = orders_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response("failed", status=401)

class client(APIView):
    # permission_classes = []
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
        if clients.objects.filter(phone_number=client_phone).exists():
            return Response({"Response": "The phone number is already registered with another client"}, status=406)
        serializer = client_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.data , status=404)

class requirements_view(APIView):
    #permission_classes = []
    def __int__(self):
        pass
    def get(self, request):
        requirements_list = requirements.objects.all()
        serializer = requirements_serializers(requirements_list, many=True)
        return Response(serializer.data)
    def post(self, request):
        user_instance = Users.objects.get(user=request.user)
        user_id = user_instance.id
        print(user_id)
        product_name = str(self.request.data["product_name"])
        quantity = int(self.request.data["quantity"])
        acceptable_by = str(self.request.data["acceptable_by"])
        request.data["user_id"] = user_id
        serializer = requirements_serializers(data=request.data)
        print(serializer.initial_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            print(serializer.errors)
            return Response(serializer.data, status=400)

@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def update_requirment_item(request,pk):
    print("xxxxxxxxxxxxxxxxx")
    user_instance = Users.objects.get(user=request.user)
    json_response = json.load(request)
    print(json_response)
    obj_list = ["product_name","quantity","acceptable_by"]
    for object in obj_list:
        # print(object)
        if object in json_response:
            #doctor_requested_id = json_response[object]
            verified_object = requirements.objects.filter(id=pk)
            verified_object.update(**json_response)
    return Response({'Response': "successfully updated."},status=200)




@api_view(['POST', ])
# @permission_classes([])
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
        return Response(data, status=201)
    else:
        return Response('password must match.', status=401)


@api_view(['POST', ])
# @permission_classes([])
def check_clientPhone(request):
    if request.method == 'POST':
        client_phone = request.data["phone"]
        if clients.objects.filter(phone_number=client_phone).exists():
            c_instance = clients.objects.get(phone_number=client_phone)
            data = {"id":c_instance.id, "name": c_instance.name, "phone_number": c_instance.phone_number, "clientlevel": c_instance.clientlevel, "notes": c_instance.notes}
            return Response(data, status=200)
        else:
            return Response({"Response": "client does not exist"}, status=404)


@api_view(['POST', ])
def search_byDate(request):
    if request.method == 'POST':
        from_date = request.data["from_date"]
        to_date = request.data["to_date"]
        state = request.data["state"]
        serializer = search_byDate_serializers(data=request.data)
        if serializer.is_valid():
            q1 = orders.objects.filter(date__range=[from_date, to_date])
            if state == 'all':
                return Response(orders_serializers(q1, many=True).data)
            elif state == 'finished':
                q2 = q1.filter(state='F')
                return Response(orders_serializers(q2, many=True).data)
            elif state == 'unfinished':
                q3 = q1.exclude(state='F')
                return Response(orders_serializers(q3, many=True).data)
            else:
                return Response({"Response": "Invalid data"}, status=404)
#   {"from_date":"2022-06-01","to_date":"2022-06-02","state":"unfinished"}
#   state=["all", "finished", "unfinished"]

@api_view(['POST', ])
def search_ByOrderId(request):
    if request.method == 'POST':
        orderId = request.data["order_id"]
        state = request.data["state"]
        serializer = orderID_serializers(data=request.data)
        if serializer.is_valid():
            q1 = orders.objects.filter(order_id=orderId)
            if state == 'all':
                return Response(orders_serializers(q1, many=True).data)
            elif state == 'finished':
                q2 = q1.filter(state='F')
                return Response(orders_serializers(q2, many=True).data)
            elif state == 'unfinished':
                q3 = q1.exclude(state='F')
                return Response(orders_serializers(q3, many=True).data)
            else:
                return Response({"Response": "Invalid data"}, status=404)
#   {"order_id":"5","state":"unfinished"}
#   state=["all", "finished", "unfinished"]

@api_view(['GET', ])
def get_unfinishedOrders(request):
    if request.method == 'GET':
        q2 = orders.objects.exclude(state='F')
        serializer = orders_serializers(q2, many=True)
        return Response(serializer.data)


@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def delete_item(request, pk):
    user_instance = Users.objects.get(user=request.user)
    if user_instance.department == 'M':
        if request.method == 'DELETE':
            item=orders.objects.filter(order_id=pk)
            item.delete()
            return Response({'Response': "successfully deleted."}, status=202)
    else:
        return Response({'Response': "You don't have permission to delete this."}, status=101)


@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def update_item(request,pk):
    user_instance = Users.objects.get(user=request.user)
    if user_instance.department == 'M':
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
        return Response({'Response': "successfully updated."},status=200)
    else:
        return Response({'Response': "You don't have permission to delete this."}, status=101)
