from django.urls import path
from . import views

#URL Configurations
urlpatterns = [
    path('hello/', views.hello_world)
]