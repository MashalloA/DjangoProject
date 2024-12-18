from django.urls import path
from . import views

urlpatterns = [
    path('' , views.book_list_view, name='books'),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),
    path('about/', views.about_me, name='about'),
    path('pets/', views.about_pets, name='pets'),
    path('time/', views.system_time, name='time'),
    path('comment/', views.comment_list_view, name='library_comment'),
    path('comment_view/', views.comment_view, name='comment_view'),
    path('search/', views.SearchView.as_view(), name='search'),
]