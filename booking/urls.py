from django.urls import path
from .views import  register, home, login,submit_appointment,appointment_success,meds,Teams

urlpatterns = [
    path('register/', register, name='register'),
    path('', login, name='login'),
    path('index/', home, name='index'),  # This should render index.html
    path('submit_appointment/', submit_appointment, name='submit_appointment'),  # Adjust the URL as needed
    path('appointment_success/', appointment_success, name='appointment_success'),
    path('meds/', meds, name='meds'),
    path('Teams/', Teams, name='Teams'),
]
