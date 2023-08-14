from django.contrib import admin

from goods.models import Categories, Characteristic, GoodsCharacteristic

from goods.models import Providers

from goods.models import Goods


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    fields = ('category_name', )


@admin.register(Providers)
class ProvidersAdmin(admin.ModelAdmin):
    fields = ('provider_name', )


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    pass


class GoodsCharacteristicInline(admin.StackedInline):
    model = GoodsCharacteristic
    extra = 1  # Количество пустых форм для добавления характеристик по умолчанию

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    inlines = [GoodsCharacteristicInline]  # Добавляем stacked inline характеристики к админской форме товара
