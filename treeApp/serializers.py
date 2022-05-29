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

# class users_serializers(serializers.ModelSerializer):
#
#     password = serializers.CharField(style={'input_type': 'password'},
#                                      write_only=True)
#
#     class Meta:
#         model = Users
#         fields = ('email', 'username','department', 'password', 'password2')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def save(self):
#         user = Users (
#             email=self.validated_data('email'),
#             username=self.validated_data('username'),
#             department=self.validated_data('department'),
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#
#         if password != password2:
#             raise serializers.ValidationError({'password': 'password must match.'})
#         Users.objects.create_user(username=user,password=password)
#         user.save()
#         return user


class orders_serializers(serializers.ModelSerializer):
    class Meta :
        model = orders
        fields = '__all__'


