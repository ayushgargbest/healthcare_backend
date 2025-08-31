from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Patient
from .serializers import PatientSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def patients_list_create(request):
    """
    GET: Get all patients created by the authenticated user
    POST: Create a new patient
    """
    if request.method == 'GET':
        patients = Patient.objects.filter(created_by=request.user)
        serializer = PatientSerializer(patients, many=True)
        return Response({
            'count': patients.count(),
            'patients': serializer.data
        }, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({
                'message': 'Patient created successfully',
                'patient': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def patient_detail_update_delete(request, patient_id):
    """
    GET: Get details of a specific patient
    PUT: Update patient details
    DELETE: Delete a patient record
    """
    patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
    
    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response({
            'patient': serializer.data
        }, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Patient updated successfully',
                'patient': serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        patient.delete()
        return Response({
            'message': 'Patient deleted successfully'
        }, status=status.HTTP_200_OK)