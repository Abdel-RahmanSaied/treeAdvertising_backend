from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response

from .models import clients
from .serializers import client_serializers

# Create your views here.

class workOrder(APIView):
    def __init__(self):
        pass
    def post(self , request):
        pass