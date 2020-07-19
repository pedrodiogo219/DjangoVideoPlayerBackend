from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.history, name='history'),
    path('add/', views.add, name='add')
]
