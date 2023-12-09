from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request,'index.html')

User = get_user_model()

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')
            elif user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def patient(request):
    return render(request,'patient.html')


def doctor(request):
    return render(request,'doctor.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def home(request):
    return render(request, 'homepage.html')