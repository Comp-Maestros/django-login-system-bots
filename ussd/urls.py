from django.urls import path
from .views import Ussd

urlpatterns = [
    path('', Ussd, name='ussd'),
]