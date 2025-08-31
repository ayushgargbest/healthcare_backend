from django.urls import path
from . import views

urlpatterns = [
    path('', views.patients_list_create, name='patients_list_create'),  # GET, POST /api/patients/
    path('<int:patient_id>/', views.patient_detail_update_delete, name='patient_detail'),  # GET, PUT, DELETE /api/patients/<id>/
]