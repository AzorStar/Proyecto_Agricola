from rest_framework import serializers
from prinapp.models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = supplier
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = driver
        fields = '__all__'

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = time
        fields = '__all__'

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = reports
        fields = '__all__'