from rest_framework import serializers
from menu_api.models import Special, Ingredient



class SpecialSerializer(serializers.ModelSerializer):
    ingredients = serializers.HyperlinkedRelatedField(
        view_name = "ingredients_detail_api_view",
        many = True,
        read_only = True

    )
    calorie_count = serializers.IntegerField()
    my_fave = serializers.SerializerMethodField()

    def get_my_fave(self, obj):
        return "Cookies"

    class Meta:
        model = Special
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
