from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from menu_api.models import Special, Ingredient
from menu_api.serializers import SpecialSerializer, IngredientSerializer

class SpecialListCreateAPIView(ListCreateAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer

class SpecialDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer

class IngredientListCreateAPIView(ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientDetailAPIView(RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
