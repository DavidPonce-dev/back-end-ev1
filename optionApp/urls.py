from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'optionApp'

urlpatterns = [
    path('tabla', TablaView.as_view(), name='tabla'),
    path('loteria', LoteriaView.as_view(), name='loteria')
]