from django.urls import path
from . import views
from .views import get_Student


urlpatterns = [
    path('students/',views.get_Student,name='students')
]