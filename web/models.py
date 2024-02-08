from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CarModel(models.Model):
    model = models.CharField(max_length=256)
    brand = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.brand} {self.model}'


class Car(models.Model):
    year = models.IntegerField(verbose_name='Год производства')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True, verbose_name='Марка, модель')
    image = models.ImageField(upload_to='car_images/', null=True, blank=True, verbose_name='Фото')


class Post(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Содержимое')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    visits = models.IntegerField(default=0)
