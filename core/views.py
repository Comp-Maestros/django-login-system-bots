from django.shortcuts import render
#add decorators to the views that require login where the login login is on a diffrent app named accounts use fucction based veiws
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from accounts.models import CustomUser


# Create your views here.
#add login decorators where the logic is on accounts app
@login_required(login_url='accounts:login')
def home(request):
    
    return render(request, 'home.html')