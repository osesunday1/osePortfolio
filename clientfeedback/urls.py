from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientfeedback, name='clientfeedback'),
]