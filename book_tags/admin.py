from django.contrib import admin
from book_tags.models import Tag, Books

admin.site.register(Tag)
admin.site.register(Books)
