"""
Views for the patient API
"""
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


from core.models import Patient
from patient import serializers


class PatientViewSet(viewsets.ModelViewSet):
    """View for manage patient apis"""
    serializer_class = serializers.PatientDeatilSerializer
    queryset = Patient.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_querset(self):
        """Retrieve patient by authentication"""
        return self.queryset.filter(patient=self.request.patient).order_by('phone_no')
    
    def get_serializer_class(self):
        """Return the serializer class for request"""
        if self.action == 'list':
            return serializers.PatientSerializer
        return self.serializer_class
        
    def perform_create(self, serializer):
        """create a new patient"""
        serializer.save(patient=self.request.patient)