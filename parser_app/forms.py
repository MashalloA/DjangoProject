from django import forms
from . import models, parser_litnet

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('litnet', 'litnet'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'litnet':
            li