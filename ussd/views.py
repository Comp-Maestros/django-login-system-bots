from django.shortcuts import render

# Create your views here.

def Ussd(request):
    return render(request, 'ussd/ussd.html')