from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Doctor
from .serializers import DoctorSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def doctors_list_create(request):
    """
    GET: Get all doctors
    POST: Create a new doctor
    """
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response({
            'count': doctors.count(),
            'doctors': serializer.data
        }, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Doctor created successfully',
                'doctor': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def doctor_detail_update_delete(request, doctor_id):
    """
    GET: Get details of a specific doctor
    PUT: Update doctor details
    DELETE: Delete a doctor record
    """
    doctor = get_object_or_404(Doctor, id=doctor_id)
    
    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response({
            'doctor': serializer.data
        }, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Doctor updated successfully',
                'doctor': serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        doctor.delete()
        return Response({
            'message': 'Doctor deleted successfully'
        }, status=status.HTTP_200_OK)