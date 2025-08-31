from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    """
    Serializer for Doctor model
    """
    class Meta:
        model = Doctor
        fields = [
            'id', 'name', 'email', 'phone', 'specialization',
            'experience_years', 'qualification', 'consultation_fee',
            'available_days', 'available_time', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_experience_years(self, value):
        if value < 0 or value > 60:
            raise serializers.ValidationError("Experience years must be between 0 and 60")
        return value
    
    def validate_consultation_fee(self, value):
        if value < 0:
            raise serializers.ValidationError("Consultation fee cannot be negative")
        return value
    
    def validate_phone(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Phone number must be at least 10 digits")
        return value