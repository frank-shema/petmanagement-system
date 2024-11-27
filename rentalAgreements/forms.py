from django import forms
from .models import RentalAgreement

class RentalAgreementForm(forms.ModelForm):
    class Meta:
        model = RentalAgreement
        fields = ['start_date', 'end_date', 'monthly_rent', 'security_deposit']
        
        # Excluded fields that would appear by default
        exclude = ['estate', 'tenant', 'owner', 'status']
