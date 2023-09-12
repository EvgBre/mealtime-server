"""mealtime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from mealtimeapi.views.auth import register_user, check_user
from mealtimeapi.views import FoodView, MealView, FoodTypeView, MealFoodView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'foods', FoodView, 'food')
router.register(r'meals', MealView, 'meal')
router.register(r'food_types', FoodTypeView, 'food_type')
router.register(r'meal_foods', MealFoodView, 'meal_food')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user)
]
