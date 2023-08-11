from rest_framework.viewsets import ModelViewSet

from goods.models import Categories
from goods.serializers import CategoriesSerializer


class CategoriesViewSet(ModelViewSet):
    queryset = Categories.object.all()
    serializer_class = CategoriesSerializer