from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from mealtimeapi.models import Meal, User


class MealView(ViewSet):
  """Bangazon API meal view"""
  
  def retrieve(self, request, pk):
    """Handle GET requests for a single meal
    
    Returns:
        Response -- JSON serialized meal
    """
    try:
        meal = Meal.objects.get(pk=pk)
        
        serializer = MealSerializer(meal)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Meal.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
  def list(self, request):
    """Handle GET requests to get all meals
    
    Returns:
        Response -- JSON serialized list of all meals
    """
    meal = Meal.objects.all()
    serializer = MealSerializer(meal, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)

  def create(self, request):
    """Handle POST operations for meal
    
    Returns:
        Response -- JSON serialized meal instance
    """
    
    userId = User.objects.get(pk=request.data["userId"])
    
    meal = Meal.objects.create(
    name=request.data["name"],
    grams=request.data["grams"],
    dow=request.data["dow"],
    meal_time=request.data["mealTime"],
    user_id=userId
    )
    serializer = MealSerializer(meal)
    return Response(serializer.data, status=status.HTTP_201_CREATED) 
    
  def update(self, request, pk):

    meal = Meal.objects.get(pk=pk)
    meal.name=request.data["name"]
    meal.grams=request.data["grams"]
    meal.dow=request.data["dow"]
    meal.meal_time=request.data["mealTime"]
    meal.user_id = User.objects.get(pk=request.data["userId"])

    meal.save()

    return Response(None, status=status.HTTP_204_NO_CONTENT)   

  def destroy(self, request, pk):
    meal = Meal.objects.get(pk=pk)
    meal.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)


class MealSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Meal
        fields = ('id', 'name', 'grams', 'dow', 'meal_time', 'user_id')
        depth = 1