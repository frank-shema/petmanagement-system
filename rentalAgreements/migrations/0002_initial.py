# Generated by Django 5.1.3 on 2024-11-26 22:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rentalAgreements', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalagreement',
            name='owner',
            field=models.ForeignKey(limit_choices_to={'role': 'admin'}, on_delete=django.db.models.deletion.CASCADE, related_name='owned_agreements', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rentalagreement',
            name='tenant',
            field=models.ForeignKey(limit_choices_to={'role': 'client'}, on_delete=django.db.models.deletion.CASCADE, related_name='agreements', to=settings.AUTH_USER_MODEL),
        ),
    ]