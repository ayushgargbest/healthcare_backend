from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctors_list_create, name='doctors_list_create'),  # GET, POST /api/doctors/
    path('<int:doctor_id>/', views.doctor_detail_update_delete, name='doctor_detail'),  # GET, PUT, DELETE /api/doctors/<id>/
]