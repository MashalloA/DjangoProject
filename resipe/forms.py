from django import forms
from .models import Recipe, Ingredient, Collection

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'recipe']

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'recipes']
