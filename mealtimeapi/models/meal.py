from django.db import models
from .user import User

class Meal(models.Model):
    name = models.CharField(max_length=100)
    grams = models.IntegerField()
    dow = models.DateField(auto_now_add=True)
    meal_time = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)