from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.all_books, name='all_books'),
    path('pensioner/', views.pensioner, name='pensioner'),
    path('youth/', views.youth, name='youth'),
    path('teenager/', views.teenager, name='teenager'),
    path('kid/', views.kid, name='kid'),
]