"""
URL routing schema for Google Auth Webapp.

"""

from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path('example', views.example, name='example'),
]
