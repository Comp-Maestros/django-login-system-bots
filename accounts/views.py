from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


# Create your views here where i want to declare my pages register and login where if the user has an account he can login and if he doesn't have an account he can register i want to have html page named login-register.html
def Register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        if password == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect('accounts:register')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already taken.')
                    return redirect('accounts:register')
                else:
                    user = CustomUser.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'Your account has been created successfully.')
                    return redirect('accounts:login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('accounts:register')
    else:
        return render(request, 'register.html')

#create for the login page
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully.')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')
    
#logout
def Logout(request):
    logout(request)
    messages.success(request, 'You have logged out successfully.')
    return redirect('accounts:login')

    