from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CarModel(models.Model):
    model = models.CharField(max_length=256)
    brand = models.CharField(max_length=256)


class Car(models.Model):
    year = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
