from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from mealtimeapi.models import MealFood, User
from mealtimeapi.views.food import FoodSerializer

class MealFoodView(ViewSet):
    """Meal Time Customer View"""
    def retrieve(self, request, pk):
        """GET request for a single meal food"""
        try:
            meal_food = MealFood.objects.get(pk=pk)
            serializer = MealFoodSerializer(meal_food)
            return Response(serializer.data)
        except MealFood.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of meal foods"""
        # user = User.objects.get(uid=uid)
        meal_foods = MealFood.objects.all()

        serializer = MealFoodSerializer(meal_foods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MealFoodSerializer(serializers.ModelSerializer):
  """JSON serializer for meal foods"""
  food_id = FoodSerializer()
  class Meta:
      model = MealFood
      fields = ('id', 'food_id', 'meal_id', 'grams')
      depth = 1