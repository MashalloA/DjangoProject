from django.contrib import admin
from . import models

admin.site.register(models.BooksModel)
admin.site.register(models.Review)