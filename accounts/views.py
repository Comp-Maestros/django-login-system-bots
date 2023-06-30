from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


# Create your views here where i want to declare my pages register and login where if the user has an account he can login and if he doesn't have an account he can register i want to have html page named login-register.html
def Register(request):
        page='register'
        #get the fields from the html page
        if request.method == 'POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email'].lower()
            password=request.POST['password']
            password2=request.POST['password2']
            #check if the passwords match
            if password == password2:
                #check if the email exists
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                else:
                    #create the user
                    user=CustomUser.objects.create_user(email=email,password=password,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,'You are now registered')
                    return redirect('accounts:login')
            else:
                messages.error(request,'Passwords do not match')
                
            context={    
                'page':page
            }
                
        return render(request,'accounts/login-register.html',   context )

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



    