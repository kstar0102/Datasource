from django.urls import path
from .views import *

#DataFlair #Url-ConfigWhen we validate our form data, we are actually c
urlpatterns = [
path('', regform, name = 'registration-form'),
]