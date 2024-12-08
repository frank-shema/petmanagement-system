from django.conf import settings
from django.db import models

class RentalAgreement(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('terminated', 'Terminated'),
        ('expired', 'Expired'),
    ]

    estate = models.ForeignKey(
        'estates.Estate',  # Use string reference instead of direct import
        on_delete=models.CASCADE,
        related_name='pet_agreements'
    )
    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'client'}, 
        related_name='agreements'
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'admin'}, 
        related_name='owned_agreements'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        db_index=True
    )

    def __str__(self):
        return f"Rental Agreement for {self.estate.property_name} - {self.tenant.username}"

    def activate(self):
        self.status = 'active'
        self.save()

    def terminate(self):
        self.status = 'terminated'
        self.save()

    def expire(self):
        self.status = 'expired'
        self.save()

    def is_active(self):
        return self.status == 'active'

    def is_pending(self):
        return self.status == 'pending'

    def is_terminated(self):
        return self.status == 'terminated'

    def is_expired(self):
        return self.status == 'expired'
