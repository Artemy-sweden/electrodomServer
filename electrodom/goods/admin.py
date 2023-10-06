from django.contrib import admin
from django.utils.safestring import mark_safe


from goods.models import Categories, Characteristic, GoodsCharacteristic, Photo, Discount

from goods.models import Providers

from goods.models import Goods


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    fields = ('category_name', )
    list_display = (Categories.__str__,)
    Categories.__str__.short_description = 'Категория'


@admin.register(Providers)
class ProvidersAdmin(admin.ModelAdmin):
    fields = ('provider_name', )
    list_display = (Providers.__str__,)
    Providers.__str__.short_description = 'Поставщик'

@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = (Characteristic.__str__,)
    Characteristic.__str__.short_description = 'Характеристика'


class GoodsCharacteristicInline(admin.StackedInline):
    model = GoodsCharacteristic
    extra = 1  # Количество пустых форм для добавления характеристик по умолчанию


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    inlines = [GoodsCharacteristicInline]
    Goods.__str__.short_description = 'Товар'
    fields = ('name', 'provider_id', 'category_id', 'price', 'count', 'description')

    # def get_html_photo(self, object):
    #     if object.commenter_avatar:
    #         return mark_safe(f"<img src='{object.image.url}' width=100>")
    #
    # get_html_photo.short_description = 'Фото'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass
