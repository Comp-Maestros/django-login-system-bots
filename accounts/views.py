from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


# Create your views here where i want to declare my pages register and login where if the user has an account he can login and if he doesn't have an account he can register i want to have html page named login-register.html
def Register(request):
    page='register'
    if request.user.is_authenticated:
        return redirect('core:home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'User account created')
            login(request,user)
            return redirect('core:home')
        else:
            messages.error(request,'An error has occured during registration')
            
    else:
        form = CustomUserCreationForm()

    return render(request,'accounts/login-register.html',{'form':form,'page':page})

def login_user(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('core:home')
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            email=request.POST['username'].lower()
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'You are logged in')
                return redirect('core:home')
            else:
                messages.error(request,'Invalid credentials')
        else:
            messages.error(request,'Invalid credentials')
            
    else:
        form = AuthenticationForm()
        
    return render(request,'accounts/login-register.html',{'form':form,'page':page})

def logout_user(request):
    logout(request)
    messages.success(request,'You are logged out')
    return redirect('core:home')



    