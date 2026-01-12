from rest_framework import serializers

from restaurant_menu.models import Product
from restaurant_menu.rest.serializers.category import (
    CategorySerializer,
    FoodCategorySerializer,
)
from restaurant_menu.rest.serializers.images import ImageSerializer
from restaurant_menu.rest.serializers.tags import TagSerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    food_category = FoodCategorySerializer(read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
