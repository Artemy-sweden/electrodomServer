from rest_framework.viewsets import ModelViewSet

from electrodom.goods.models import Categories


class CategoriesViewSet(ModelViewSet):
    queryset = Categories.object.all()
    serializer_class = CategoriesSerializer
