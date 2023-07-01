from django.urls import path
from .views import ussd_callback

app_name = 'ussd'

urlpatterns = [
    path('ussd_callback', ussd_callback, name='ussd_callback'),
]