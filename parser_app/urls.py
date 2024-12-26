from django.urls import path
from . import views

urlpatterns = [
    path('manga_list/', views.MainListView.as_view(), name='manga_list'),
    path('form_parser_manga/', views.MangaFormView.as_view()),
]