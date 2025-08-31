from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, PatientDoctorMappingCreateSerializer
from patients.models import Patient
from doctors.models import Doctor

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def mappings_list_create(request):
    """
    GET: Get all patient-doctor mappings for authenticated user's patients
    POST: Assign a doctor to a patient
    """
    if request.method == 'GET':
        mappings = PatientDoctorMapping.objects.filter(
            patient__created_by=request.user,
            is_active=True
        )
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response({
            'count': mappings.count(),
            'mappings': serializer.data
        }, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = PatientDoctorMappingCreateSerializer(data=request.data)
        if serializer.is_valid():
            # Verify that the patient belongs to the authenticated user
            patient = serializer.validated_data['patient']
            if patient.created_by != request.user:
                return Response({
                    'error': 'You can only assign doctors to your own patients'
                }, status=status.HTTP_403_FORBIDDEN)
            
            mapping = serializer.save()
            response_serializer = PatientDoctorMappingSerializer(mapping)
            
            return Response({
                'message': 'Patient assigned to doctor successfully',
                'mapping': response_serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_patient_doctors(request, patient_id):
    """
    Get all doctors assigned to a specific patient
    """
    patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
    mappings = PatientDoctorMapping.objects.filter(
        patient=patient,
        is_active=True
    )
    serializer = PatientDoctorMappingSerializer(mappings, many=True)
    
    return Response({
        'patient_name': patient.name,
        'assigned_doctors_count': mappings.count(),
        'mappings': serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_mapping(request, mapping_id):
    """
    Remove a doctor from a patient
    """
    mapping = get_object_or_404(
        PatientDoctorMapping, 
        id=mapping_id,
        patient__created_by=request.user
    )
    mapping.is_active = False
    mapping.save()
    
    return Response({
        'message': 'Doctor removed from patient successfully'
    }, status=status.HTTP_200_OK).save()
    
    return Response({
        'message': 'Doctor removed from patient successfully'
    }, status=status.HTTP_200_OK)