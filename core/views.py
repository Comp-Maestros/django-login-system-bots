from django.shortcuts import render

# Create your views here.

#create home page with function based view home.html
def home(request):
    return render(request,'home.html')
