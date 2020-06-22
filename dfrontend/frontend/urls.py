from django.urls import path
from . import views

urlpatterns = [
    path('', views.fe,name='frontend homepage'),
]
