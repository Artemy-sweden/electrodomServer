from django.contrib import admin
from django.utils.safestring import mark_safe

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
    inlines = [GoodsCharacteristicInline]
    Goods.__str__.short_description = 'Товар'
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.commenter_avatar:
            return mark_safe(f"<img src='{object.image.url}' width=100>")

    get_html_photo.short_description = 'Фото'
