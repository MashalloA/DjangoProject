from django.db import models
from book_tags.models import Books

class BasketModel(models.Model):
    CHECKING = (
        ('✅','✅'),
        ('❌','❌'),
    )
    name = models.CharField(max_length=100, verbose_name='ваше имя')
    email = models.EmailField(verbose_name='ваша электронная почта')
    phone_number = models.IntegerField(verbose_name='ваш номер телефона')
    book = models.URLField(verbose_name="укажите ссылку на книгу", null=True)
    library = models.ForeignKey(Books, on_delete=models.CASCADE, null=True)
    choice_check = models.CharField(max_length=10, choices=CHECKING, null=True)

    def __str__(self):
        return self.name

