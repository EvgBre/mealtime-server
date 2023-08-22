from django.db import models
from user import User
from food_type import FoodType

class Food(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=3000)
    type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    