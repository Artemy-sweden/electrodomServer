from rest_framework.viewsets import ModelViewSet

from goods.models import Categories
from goods.serializers import CategorySerializer
from goods.serializers import ProviderSerializer

from goods.models import Providers


class CategoriesViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class ProvidersViewSet(ModelViewSet):
    queryset = Providers.objects.all()
    serializer_class = ProviderSerializer


