from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    """
    Serializer for PatientDoctorMapping model
    """
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'doctor', 'patient_details', 'doctor_details',
            'assigned_date', 'notes', 'is_active'
        ]
        read_only_fields = ['id', 'assigned_date']
    
    def validate(self, attrs):
        # Check if this mapping already exists
        patient = attrs.get('patient')
        doctor = attrs.get('doctor')
        
        if PatientDoctorMapping.objects.filter(
            patient=patient, 
            doctor=doctor, 
            is_active=True
        ).exists():
            raise serializers.ValidationError(
                "This patient is already assigned to this doctor"
            )
        
        return attrs

class PatientDoctorMappingCreateSerializer(serializers.ModelSerializer):
    """
    Simplified serializer for creating mappings
    """
    class Meta:
        model = PatientDoctorMapping
        fields = ['patient', 'doctor', 'notes']