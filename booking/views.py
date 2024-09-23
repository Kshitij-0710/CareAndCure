from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import UserRegistrationForm, AppointmentForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])  # Hash the password
            user.save()

            # Automatically log in the user after registration
            auth_login(request, user)
            return redirect("index")  # Redirect to home after registration
    else:
        form = UserRegistrationForm()
    
    return render(request, "register.html", {"form": form})

@login_required
def home(request):
    form = AppointmentForm()  # Create an instance of the form
    return render(request, 'index.html', {'form': form})  # Pass the form to the template

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Redirect to index.html after successful login
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

@login_required
def submit_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  
            appointment.save()

            # Send email to the doctor and the user
            doctor_email = form.cleaned_data['doctor_email']
            user_email = request.user.email  # Get the logged-in user's email
            sender_email = 'careandcure@woxsen.edu.in'

            try:
                send_mail(
                    'Appointment Booking Confirmation',
                    f'Dear {request.user.username},\n\nYour appointment has been booked.',
                    sender_email,
                    [doctor_email, user_email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Error sending email: {e}")

            return redirect('appointment_success')  # Adjust as necessary
        else:
            print(form.errors)  # This will print out any validation errors in the terminal
    else:
        form = AppointmentForm()

    return render(request, 'index.html', {'form': form})

def appointment_success(request):
    return render(request, 'as.html')  # Create this template for confirmation
def meds(request):
    return render(request,'medicine.html')
def Teams(request):
    return render(request, 'teams.html')