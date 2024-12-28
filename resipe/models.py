from django.db import models


class Recipe(models.Model):
    title = models.TextField(verbose_name='название рецепта')
    description = models.CharField(max_length=100, verbose_name='описание рецепта')

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    UNIT = (
        ("граммы", "граммы"),
        ("килограммы", "килограммы"),
        ("миллилитры", "миллилитры"),
        ("литры", "литры"),
        ("штуки", "штуки")
    )

    name = models.CharField(max_length=100, verbose_name="название ингредиента", null=True)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50, choices=UNIT, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    is_optional = models.BooleanField(default=False)
    calories = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.quantity} {self.unit}"


class Collection(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe, related_name='collections')
    def __str__(self):
        return self.name