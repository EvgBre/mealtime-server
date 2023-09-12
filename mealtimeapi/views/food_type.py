from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mealtimeapi.models import FoodType


class FoodTypeView(ViewSet):
    """Bangazon API catgory view"""
    
    def retrieve(self, request, pk):
      """Handle GET requests for a single food type
      
      Returns:
          Response -- JSON serialized food type
      """
      
      try:
          food_type = FoodType.objects.get(pk=pk)
          
          serializer = FoodTypeSerializer(food_type)
          return Response(serializer.data, status=status.HTTP_200_OK)
        
      except FoodType.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
      """Handle GET requests to get all food types
      
      Returns:
          Response -- JSON serialized list of all food types
      """
      
      categories = FoodType.objects.all()
      
      serializer = FoodTypeSerializer(categories, many=True)
      return Response(serializer.data)

class FoodTypeSerializer(serializers.ModelSerializer):
  """JSON serializer for food types"""
  
  class Meta:
      model = FoodType
      fields = ('id', 'label')
      depth = 0