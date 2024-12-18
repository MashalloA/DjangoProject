from django import forms
from library_blog.models import Review


class LibraryForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'