from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm,LoginForm


# Create your views here where i want to declare my pages register and login where if the user has an account he can login and if he doesn't have an account  use forms.py
def Register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request,'accounts/register.html',{'form':form})

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email,password=password)
        if user:
            login(request,user)
            messages.success(request,'Login successfully')
            return redirect('accounts:login')
        else:
            messages.error(request,'Invalid email or password')
            return redirect('accounts:login')
    return render(request,'accounts/login.html')

def Logout(request):
    logout(request)
    messages.success(request,'Logout successfully')
    return redirect('accounts:login')

    