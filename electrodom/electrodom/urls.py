
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from user.views import UserViewSet, CommentViewSet, BasketViewSet
from goods.views import CategoriesViewSet
from goods.views import ProvidersViewSet


router = DefaultRouter()
router.register('categories', CategoriesViewSet)
router.register('users', UserViewSet)
router.register('comments', CommentViewSet)
router.register('providers', ProvidersViewSet)
router.register('baskets', BasketViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls

