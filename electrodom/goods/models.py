from django.db import models


# class DBMixin(models.Model):
#     # using = 'default'  # По умолчанию, используем default базу данных
#
#     class Meta:
#         abstract = True
#
#     def save(self, *args, **kwargs):
#         using_db = getattr(self, 'using', self.using)
#         super().save(using=using_db, *args, **kwargs)


class Providers(models.Model):
    provider_name = models.CharField(max_length=255)


class Categories(models.Model):
    category_name = models.CharField(max_length=255)


class Characteristic(models.Model):
    name = models.CharField(max_length=50)


class Goods(models.Model):
    name = models.CharField(max_length=255)
    provider_id = models.ForeignKey(to=Providers, on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(to=Categories, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(decimal_places=2, max_digits=6)
    count = models.PositiveIntegerField()
    description = models.TextField()


class GoodsCharacteristic(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)
