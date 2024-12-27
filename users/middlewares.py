from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class LevelMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = int(request.POST.get('experience'))
            if experience < 2:
                return HttpResponseBadRequest('Извините вашего опыта не хватает приходите на следующий год')
            elif experience >2 and experience < 4:
                request.level = 'Junior'
            elif experience >4 and experience < 8:
                request.level = 'Middle'
            elif experience >8 and experience < 50:
                request.level = 'Senior'
            else:
                return HttpResponseBadRequest('Извините ваш возраст больше 50 вы нам не подходите')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request,'level','Уровень не определен.')