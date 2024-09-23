from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Appointment

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@woxsen.edu.in'):
            raise ValidationError("Please enter your woxsen mail id")
        return email

from django import forms
from .models import Appointment  # Ensure this is your correct model import

class AppointmentForm(forms.ModelForm):
    DOCTORS_CHOICES = [
        ('Doc1@woxse.edu.in', 'Dr.Thota Srikar'),
        ('Doc2@woxsen.edu.in', 'Dr.Murali'),
        ('Doc3@woxsen.edu.in', 'Dr. Mahita'),
    ]

    TIME_SLOT_CHOICES = [
        ('9:00 AM', '9:00 AM'),
        ('10:00 AM', '10:00 AM'),
        ('11:00 AM', '11:00 AM'),
        ('2:00 PM', '2:00 PM'),
        ('3:00 PM', '3:00 PM'),
    ]

    doctor_email = forms.ChoiceField(choices=DOCTORS_CHOICES, label="Doctor's Name")
    time_slot = forms.ChoiceField(choices=TIME_SLOT_CHOICES, label="Choose Time Slot")
    appointment_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Choose Date",
        input_formats=['%Y-%m-%d']  # This ensures the date is submitted in the format Django expects
    )

    class Meta:
        model = Appointment
        fields = ['doctor_email', 'time_slot', 'appointment_date']

