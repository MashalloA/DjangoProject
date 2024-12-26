from django import forms
from . import models, parser_manga

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('manga', 'manga'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]
    def parser_data(self):
        if self.cleaned_data['media_type'] == 'manga':
            manga_file = parser_manga.parsing()
            for i in manga_file:
                models.MangaModel.objects.create(**i)