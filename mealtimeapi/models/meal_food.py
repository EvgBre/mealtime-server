from django.db import models
from .food import Food
from .meal import Meal

class MealFood(models.Model):
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE)
    grams = models.IntegerField()