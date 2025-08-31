from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer for Patient model
    """
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'id', 'name', 'email', 'phone', 'age', 'gender', 
            'address', 'medical_history', 'created_by', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']
    
    def validate_age(self, value):
        if value < 0 or value > 150:
            raise serializers.ValidationError("Age must be between 0 and 150")
        return value
    
    def validate_phone(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Phone number must be at least 10 digits")
        return value