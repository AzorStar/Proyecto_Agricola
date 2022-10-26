from dataclasses import field
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#para todos los campos: '__all__'
#para uno en especifico: ['campo', 'campo2']