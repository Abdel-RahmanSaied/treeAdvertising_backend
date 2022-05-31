from rest_framework import serializers
from .models import clients
from .models import Users
from .models import orders
from django.contrib.auth.models import User

class client_serializers(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = '__all__'

class users_serializers(serializers.ModelSerializer):


    class Meta:
        model = Users
        fields = '__all__'

# class users_serializers(serializers.ModelSerializer):
#
#     password = serializers.CharField(style={'input_type': 'password'},
#                                      write_only=True)
#
#     class Meta:
#         model = Users
#         fields = ('name', 'username', 'password', 'password2')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def save(self):
#         user = User (
#             username=self.validated_data('username'),
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#
#         if password != password2:
#             raise serializers.ValidationError({'password': 'password must match.'})
#         user.save()
#         return user


class orders_serializers(serializers.ModelSerializer):
    class Meta :
        model = orders
        fields = '__all__'


