from django.urls import path
from .views import *



urlpatterns = [
    path('', getRoute, name="routes")
]
