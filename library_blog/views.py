from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def about_me(request):
    if request.method == "GET":
        return HttpResponse("Привет, я Машалло Алим и это мой проект 4-месяца")

def about_pets(request):
    if request.method == "GET":
        return HttpResponse("Кошка: черного цвета с красивыми глазами, очень игривая и постоянно голодная."
                            "Возраст: не знаю, примерно 3 месяца")

def system_time(request):
    if request.method == "GET":
        now_time = datetime.now().time()
        return HttpResponse(f"текущее время: {now_time}")
