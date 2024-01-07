from django.urls import path
from .views import *



urlpatterns = [
    path('', getRoute, name="routes"),
    path('notes/',getNotes),
    path('note/<int:pk>/',getNote),
]
