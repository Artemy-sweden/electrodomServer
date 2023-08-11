from django.db import models

from goods.models import Goods


# class DBMixin(models.Model):
#     using = 'default'  # По умолчанию, используем default базу данных
#
#     class Meta:
#         abstract = True
#
#     def save(self, *args, **kwargs):
#         using_db = getattr(self, 'using', self.using)
#         super().save(using=using_db, *args, **kwargs)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='users_photos', blank=True)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    # using = 'users'


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    comment_text = models.TextField(verbose_name='Текст')
    comment_date = models.DateTimeField(verbose_name='Дата создания')
    # using = 'users'


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    goods = models.ForeignKey(to=Goods, on_delete=models.CASCADE, null=False)
    count = models.PositiveSmallIntegerField()
    # using = 'users'

