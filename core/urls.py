#import path    
from django.urls import path
#import home views.py
from . import views

#app name should be core
app_name = 'core'

#path for home page
urlpatterns = [
    path('',views.home,name='home'),
]
