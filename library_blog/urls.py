from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_me, name='about'),
    path('pets/', views.about_pets, name='pets'),
    path('time/', views.system_time, name='time'),
]