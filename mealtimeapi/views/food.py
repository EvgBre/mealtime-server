from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count,Q
from rest_framework import serializers, status
from mealtimeapi.models import  User, Food, FoodType, Meal, MealFood


class FoodView(ViewSet):
    """Meal time food view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single food
        Returns:
            Response -- JSON serialized food
        """
        try:
            food = Food.objects.get(pk=pk)
            serializer = FoodSerializer(food)
            return Response(serializer.data)
        except Food.DoesNotExist:
          return Response({'message': 'Food does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all foods

        Returns:
            Response -- JSON serialized list of foods
        """
        foods = Food.objects.all()
        # uid = request.META['HTTP_AUTHORIZATION']
        # user = User.objects.get(uid=uid)
        # meals = Meal.objects.filter(user_id=user)
        meal_id = request.query_params.get('meal_id')
        if meal_id is not None:
            meal_foods = MealFood.objects.filter(meal_id=meal_id)
            foods = []
            for food in meal_foods:
                foods.append(food.food_id)

        serializer = FoodSerializer(foods, many=True, context={'request': request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    
    def create(self, request):
 
       
        userId = User.objects.get(pk=request.data["userId"])
        foodType = FoodType.objects.get(pk=request.data["foodType"])

        food = Food.objects.create(
            name=request.data["name"],
            image_url=request.data["imageUrl"],
            type=foodType,
            user_id=userId
        )
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    def update(self, request, pk):

        food = Food.objects.get(pk=pk)
        food.name = request.data["name"]
        food.image_url=request.data["imageUrl"]
        food.type=FoodType.objects.get(pk=request.data["foodType"])
        food.user_id= User.objects.get(pk=request.data["userId"])

        food.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)   
    
    def destroy(self, request, pk):
        food = Food.objects.get(pk=pk)
        food.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def add(self, request, pk):
            """Post request for a user to add a food to a meal"""

            food = Food.objects.get(pk=pk)
            meal = Meal.objects.get(pk=request.data["mealId"])
            MealFood.objects.create(
                food_id=food,
                meal_id=meal,
                grams=request.data["grams"]
        )
            return Response({'message': 'Added to Meal'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def remove(self, request, pk):
            """Delete request for a user to remove a food from a meal"""

            food = Food.objects.get(pk=request.data["foodId"])
            meal = Meal.objects.get(pk=request.data["mealId"])
            try:
                meal_food = MealFood.objects.get(food_id=food, meal_id=meal)
                meal_food.delete()
                return Response({'message': 'Removed from Meal'}, status=status.HTTP_204_NO_CONTENT)
            except MealFood.DoesNotExist:
                return Response({'message': 'MealFood not found'}, status=status.HTTP_404_NOT_FOUND)

class FoodSerializer(serializers.ModelSerializer):
    """JSON serializer for foods
    """
    class Meta:
        model = Food
        fields = ('id', 'name', 'image_url', 'type', 'user_id')
        depth = 1
        