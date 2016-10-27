from rest_framework import serializers
from menu_api.models import Special, Ingredient



class SpecialSerializer(serializers.ModelSerializer):
    ingredients = serializers.HyperlinkedRelatedField(
        view_name = "ingredients_detail_api_view",
        many = True,
        read_only = True

    )
    #created_by = serializers.ReadOnlyField()
    calorie_count = serializers.ReadOnlyField()
    my_fave = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='created_by.id')

    def get_my_fave(self, obj):
        return "Cookies"

    class Meta:
        model = Special
        exclude = ('created_by', )

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
