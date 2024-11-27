from rest_framework import serializers
from estates.models import Estate
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = ['id', 'property_name', 'address', 'property_type', 'rent_amount','owner']