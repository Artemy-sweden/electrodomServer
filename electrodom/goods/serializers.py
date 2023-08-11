from rest_framework import serializers

from goods.models import Categories


class CategoriesSerializer(serializers.Serializer):
    class Meta:
        model = Categories
        fields = ['id', 'category_name']
