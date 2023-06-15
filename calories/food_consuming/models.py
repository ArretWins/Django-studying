from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()


class FoodConsumed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
