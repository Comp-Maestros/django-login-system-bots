#add path
from django.urls import path
from .views import Register,Login,Logout

app_name='accounts'

urlpatterns = [
    path('register/',Register,name='register'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
]