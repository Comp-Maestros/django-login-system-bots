#add path
from django.urls import path
from .views import Register,login_user,logout_user

app_name='accounts'

urlpatterns = [
    path('register/',Register,name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
]