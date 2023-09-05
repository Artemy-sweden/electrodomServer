from rest_framework import serializers
from goods.models import Categories, Characteristic, GoodsCharacteristic, Photo

from goods.models import Providers

from goods.models import Goods


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'category_name']


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Providers
        fields = ['id', 'provider_name']


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'


class GoodsCharacteristicSerializer(serializers.ModelSerializer):
    characteristic = CharacteristicSerializer()

    class Meta:
        model = GoodsCharacteristic
        fields = ['characteristic', 'value']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'path']


class GoodsSerializer(serializers.ModelSerializer):
    characteristics = GoodsCharacteristicSerializer(many=True, source='goodscharacteristic_set', required=False)
    category = CategorySerializer(source='category_id')

    product_images = serializers.SerializerMethodField()
    general_images = serializers.SerializerMethodField()

    def get_product_images(self, obj):
        # Filter product images where for_card=True
        product_images = obj.photo_set.filter(for_card=True)
        return PhotoSerializer(product_images, many=True).data

    def get_general_images(self, obj):
        # Filter general images where for_card=False
        general_images = obj.photo_set.filter(for_card=False)
        return PhotoSerializer(general_images, many=True).data

    class Meta:
        model = Goods
        fields = ['id', 'name', 'provider_id', 'category', 'price', 'count', 'description',
                  'characteristics', 'product_images', 'general_images']


class GoodsShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'name', 'description']

