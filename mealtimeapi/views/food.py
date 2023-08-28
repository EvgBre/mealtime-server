from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from mealtimeapi.models import  User, Food, FoodType, Meal, MealFood


class ProductView(ViewSet):
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
        uid = request.META['HTTP_AUTHORIZATION']
        user = User.objects.get(uid=uid)
        meals = Meal.objects.filter(user_id=user)
        for food in foods:
            food.inmeal = len(MealFood.objects.filter(
            meal_id__in=meals,  # Using the retrieved Order instances
            food_id=food,
        )) > 0
        serializer = FoodSerializer(foods, many=True)
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
        food.type=FoodType.objects.get(pk=request.data["price"])
        food.user_id= User.objects.get(pk=request.data["userId"])

        food.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)   
    
    def destroy(self, request, pk):
        food = Food.objects.get(pk=pk)
        food.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    # @action(methods=['post'], detail=True)
    # def favorite(self, request, pk):
    #     """Post request for a user to sign up for an event"""

    #     user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
    #     product = Product.objects.get(pk=pk)
    #     FavoriteProduct.objects.create(
    #         product=product,
    #         user=user
    # )
    #     return Response({'message': 'Made favorite'}, status=status.HTTP_201_CREATED)

    # @action(methods=['delete'], detail=True)
    # def unfavorite(self, request, pk):
    #     """Delete request for a user to leave an event"""

    #     user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
    #     product = Product.objects.get(pk=pk)
    #     favorite = FavoriteProduct.objects.get(
    #         product=product,
    #         user=user
    #     )
    #     favorite.delete()

    #     return Response({'message': 'Remove favorite'}, status=status.HTTP_204_NO_CONTENT)

class FoodSerializer(serializers.ModelSerializer):
    """JSON serializer for foods
    """
    class Meta:
        model = Food
        fields = ('id', 'name', 'image_url', 'type', 'user_id')
        depth = 1