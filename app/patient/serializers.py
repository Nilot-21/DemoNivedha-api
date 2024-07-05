"""
Serializers for patient apis
"""
from rest_framework import serializers

from core.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for patient"""

    class Meta:
        model = Patient
        fileds = ['patient_name', 'phone_no', 'address', 'landmark', 'country', 'city', 'state', 'pincode']
        read_only_fields = ['phone_no'] 


class PatientDeatilSerializer(PatientSerializer):
    """Seraializer for the patient detail view"""

    class Meta:
        fields = PatientSerializer.Meta.fileds