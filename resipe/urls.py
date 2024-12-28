from django.urls import path
from . import views


urlpatterns = [
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/new/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('collections/', views.CollectionListView.as_view(), name='collection_list'),
    path('collections/new/', views.CollectionCreateView.as_view(), name='collection_create'),
]
