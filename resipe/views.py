from django.views.generic import ListView, DetailView, CreateView
from .models import Recipe
from .forms import RecipeForm
from django.urls import reverse_lazy
from .forms import CollectionForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe_list')


class CollectionCreateView(CreateView):
    model = CollectionForm
    form_class = CollectionForm
    template_name = 'collections/collection_form.html'
    success_url = reverse_lazy('collection_list')


class CollectionListView(ListView):
    model = CollectionForm
    template_name = 'collections/collection_list.html'
    context_object_name = 'collections'