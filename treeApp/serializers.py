from rest_framework import serializers
from .models import clients
from .models import Users
from .models import orders
from .models import requirements
from django.contrib.auth.models import User

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

class requirements_serializers(serializers.ModelSerializer):
    class Meta :
        model = requirements
        fields = '__all__'

class search_byDate_serializers(serializers.Serializer):
    class Meta :
        from_date = serializers.DateField()
        to_date = serializers.DateField()
        state = serializers.CharField(max_length=255)

class orderID_serializers(serializers.Serializer):
    class Meta :
        order_id = serializers.IntegerField()
        state = serializers.CharField(max_length=255)