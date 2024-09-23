from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)  
    doctor_email = models.EmailField()
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date}"
    
# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    patient_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
