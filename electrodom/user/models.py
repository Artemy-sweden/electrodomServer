from django.db import models

from electrodom.goods.models import Goods


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='users_photos')
    phone_number = models.CharField(max_length=13)
    address = models.TextField()

    class Meta:
        app_label = 'user'
        using = 'users'


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    comment_text = models.TextField(verbose_name='Текст')
    comment_date = models.DateTimeField(verbose_name='Дата создания')

    class Meta:
        app_label = 'user'
        using = 'users'


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    goods = models.ForeignKey(to=Goods, on_delete=models.CASCADE, null=False)
    count = models.PositiveSmallIntegerField()

    class Meta:
        app_label = 'user'
        using = 'users'
