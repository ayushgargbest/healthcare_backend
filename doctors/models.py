from django.db import models

class Doctor(models.Model):
    """
    Doctor model to store doctor information
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=255)
    experience_years = models.IntegerField()
    qualification = models.CharField(max_length=255)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    available_days = models.CharField(max_length=255, help_text="e.g., Mon-Fri, Weekend")
    available_time = models.CharField(max_length=255, help_text="e.g., 9 AM - 5 PM")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"
    
    class Meta:
        ordering = ['name']