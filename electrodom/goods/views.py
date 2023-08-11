from rest_framework.viewsets import ModelViewSet

from goods.models import Categories
from goods.serializers import CategorySerializer


class CategoriesViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


