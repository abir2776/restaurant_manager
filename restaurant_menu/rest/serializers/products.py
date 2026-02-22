from rest_framework import serializers

from restaurant_menu.models import Product
from restaurant_menu.rest.serializers.category import (
    CategorySerializer,
)
from restaurant_menu.rest.serializers.images import ImageSerializer
from restaurant_menu.rest.serializers.tags import TagSerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    category_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
    )
    images_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
    )
    tags_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
    )

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        category_ids = validated_data.pop("category_ids", [])
        image_ids = validated_data.pop("images_ids", [])
        tag_ids = validated_data.pop("tags_ids", [])

        product = super().create(validated_data)

        if category_ids:
            product.category.set(category_ids)

        if image_ids:
            product.images.set(image_ids)

        if tag_ids:
            product.tags.set(tag_ids)

        return product

    def update(self, instance, validated_data):
        category_ids = validated_data.pop("category_ids", None)
        image_ids = validated_data.pop("images_ids", None)
        tag_ids = validated_data.pop("tags_ids", None)

        instance = super().update(instance, validated_data)

        if category_ids is not None:
            instance.category.set(category_ids)

        if image_ids is not None:
            instance.images.set(image_ids)

        if tag_ids is not None:
            instance.tags.set(tag_ids)

        return instance
