from django.db import models
from users.models import User

class Estate(models.Model):
    property_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='estates')
    property_type = models.CharField(max_length=50, choices=[('House', 'House'), ('Apartment', 'Apartment')])
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    property_image = models.ImageField(upload_to='property_images/', blank=True, null=True)

    @property
    def is_available(self):
        """Check if the estate is available for rent"""
        return not self.pet_agreements.filter(status='active').exists()  # Corrected related_name

    @property
    def current_agreement(self):
        """Get the current active rental agreement if any"""
        return self.pet_agreements.filter(status='active').first()  # Corrected related_name

    def __str__(self):
        return self.property_name



