from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    photo = models.CharField(max_length=5000)
    diet = models.CharField(max_length=50)
    uid = models.CharField(max_length=100)