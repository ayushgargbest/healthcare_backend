from django.urls import path
from . import views

urlpatterns = [
    path('', views.mappings_list_create, name='mappings_list_create'), 
    path('<int:patient_id>/', views.get_patient_doctors, name='get_patient_doctors'),  
    path('<int:mapping_id>/', views.remove_mapping, name='remove_mapping'),  
]