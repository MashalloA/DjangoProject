from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    phone_number = models.CharField(max_length=14, unique=True)
    age = models.PositiveIntegerField(default=16)
    experience = models.PositiveIntegerField(default=1, verbose_name='Укажите стаж работы')
    gender = models.CharField(max_length=10, choices=GENDER, default='Other')
    level = models.CharField(max_length=100, default='Уровень не определен')

    def save(self, *args, **kwargs):
        if self.experience < 2:
            self.level = 'Извините вашего опыта не хватает'
        elif 2 <= self.experience <= 4:
            self.level = 'Junior'
        elif 4 <= self.experience <= 8:
            self.level = 'Middle'
        elif 8 <= self.experience <= 50:
            self.level = 'Senior'
        else:
            self.level = 'Извините ваш возраст больше 50 вы нам не подходите.'

        super().save(*args, **kwargs)