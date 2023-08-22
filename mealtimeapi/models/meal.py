from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    grams = models.IntegerField()
    dow = models.DateField(auto_now_add=True)
    meal_time = models.CharField(max_length=50)