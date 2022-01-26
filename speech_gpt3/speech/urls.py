from django.urls import path
from .views import main

# URLConf
urlpatterns = [
    path('hello/', main)
]