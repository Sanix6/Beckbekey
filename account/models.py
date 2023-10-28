from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    name = models.CharField('Аты', max_length=100)
    phone = models.CharField("Телефон", unique=True, max_length=20)
    number = models.CharField("Телефон", max_length=20)
    code = models.CharField("Код активации", max_length=6, null=True, blank=True)
    address = models.EmailField("Электрондук адрес")
    type_massage = [
        ('Арыз', 'Арыз'),
        ('Сунуш-пикир', 'Сунуш-пикир'),
        ('Пикир', 'Пикир')
    ]
    massage = models.CharField('Билдируунун темасы', max_length=255, choices=type_massage)
    Image = models.ImageField('Фото тиркоо')
    text = models.CharField('Текст', max_length=1000)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.phone},{self.name},{self.address},{self.massage},{self.Image},{self.text},{self.code}'
