from rest_framework import serializers
from .models import clients
from .models import Users
from .models import orders

class client_serializers(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = '__all__'

class users_serializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class orders_serializers(serializers.ModelSerializer):
    class Meta :
        model = orders
        fields = '__all__'
