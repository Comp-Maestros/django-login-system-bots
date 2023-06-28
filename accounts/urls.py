#add path
from django.urls import path
#import views.py
from . import views

#app name should be accounts
app_name = 'accounts'

#path for register page
urlpatterns = [
    path('register/',views.register,name='register'),
]