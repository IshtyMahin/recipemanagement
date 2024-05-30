from rest_framework import serializers

from .models import Ingredients, Recipes, Ratings, Comments
from member.serializers import UserSerializer


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    chief = UserSerializer(read_only=True)
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipes
        fields = '__all__'

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        recipe = Recipes.objects.create(**validated_data)
        for data in ingredients:
            ingredient, created = Ingredients.objects.get_or_create(**data)
            recipe.ingredients.add(ingredient)
        return recipe

class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Ratings
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = '__all__'
