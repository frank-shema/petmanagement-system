from django import forms
from .models import Estate

class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = ['property_name', 'address', 'property_type', 'rent_amount', 'property_image']
        widgets = {
            'property_type': forms.Select(choices=[('House', 'House'), ('Apartment', 'Apartment')]),
        }
