from django.db import models


class Providers(models.Model):
    provider_name = models.CharField(max_length=255)

    class Meta:
        app_label = 'goods'
        using = 'default'


class Categories(models.Model):
    category_name = models.CharField(max_length=255)

    class Meta:
        app_label = 'goods'
        using = 'default'


class Goods(models.Model):
    name = models.CharField(max_length=255)
    provider_id = models.ForeignKey(to=Providers, on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(to=Categories, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    count = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        app_label = 'goods'
        using = 'default'