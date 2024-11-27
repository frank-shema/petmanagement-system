from rest_framework import serializers
from .models import RentalAgreement
from estates.serializers import EstateSerializer,CustomUserSerializer


class RentalAgreementSerializer(serializers.ModelSerializer):
    estate = EstateSerializer()
    class Meta:
        model = RentalAgreement
        fields = [
            'id', 'estate', 'tenant', 'owner', 'start_date', 'end_date', 
            'monthly_rent', 'security_deposit', 'status'
        ]
