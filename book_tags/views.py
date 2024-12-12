from django.shortcuts import render
from . import models

def all_books(request):
    if request.method == "GET":
        books = models.Books.objects.all().order_by('-id')
        context = {'all_books': books}
        return render(request,
                    template_name='tags/all_books.html',
                    context=context
        )

def pensioner(request):
    if request.method == "GET":
        for_pensioner = models.Books.objects.filter(tags__name='для пенсионеров').order_by('-id')
        context = {'for_pensioner': for_pensioner}
        return render(request,
                      template_name='tags/pensioners.html',
                      context=context
        )

def youth(request):
    if request.method == "GET":
        for_youth = models.Books.objects.filter(tags__name='для молодёжи').order_by('-id')
        context = {'for_youth': for_youth}
        return render(request,
                      template_name='tags/youths.html',
                      context=context
        )

def teenager(request):
    if request.method == "GET":
        for_teenager = models.Books.objects.filter(tags__name='для подростков').order_by('-id')
        context = {'for_teenager': for_teenager}
        return render(request,
                      template_name='tags/teenagers.html',
                      context=context
        )

def kid(request):
    if request.method == "GET":
        for_kid = models.Books.objects.filter(tags__name='для детей').order_by('-id')
        context = {'for_kid': for_kid}
        return render(request,
                      template_name='tags/kids.html',
                      context=context
        )