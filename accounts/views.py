from django.shortcuts import render

# Create your views here.

#create a register page with function based view register.html
def register(request):
    return render(request,'register.html')
    