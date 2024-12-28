from django.views.generic import ListView, DetailView, CreateView
from .models import Recipe
from .forms import RecipeForm
from django.urls import reverse_lazy
from .forms import CollectionForm



class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Recipe.objects.filter(title__icontains=query)
        return Recipe.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['total_calories'] = sum(
            ingredient.calories for ingredient in recipe.ingredients.all() if ingredient.calories
        )
        return context

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