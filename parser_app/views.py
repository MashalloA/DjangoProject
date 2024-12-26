from django.shortcuts import render, HttpResponse
from . import models, forms
from django.views import generic

class MainListView(generic.ListView):
    template_name = 'parser/manga_list.html'
    context_object_name = 'manga'
    model = models.MangaModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class MangaFormView(generic.FormView):
    template_name = 'parser/manga_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('STATUS 200')
        else:
            return super(MangaFormView, self).post(request, *args, **kwargs)