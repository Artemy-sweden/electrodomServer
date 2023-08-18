from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


from rest_framework.authtoken.models import Token

from goods.models import Goods


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='users_photos', blank=True, verbose_name='Фото')
    phone_number = models.CharField(max_length=13, blank=True, verbose_name='Телефон')
    address = models.TextField(blank=True, verbose_name='Адрес')
    email = models.EmailField(unique=True, verbose_name='Почта')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, verbose_name='Пользователь')
    comment_text = models.TextField(verbose_name='Текст')
    comment_date = models.DateTimeField(verbose_name='Дата создания')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.user


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, verbose_name='Пользователь')
    goods = models.ForeignKey(to=Goods, on_delete=models.CASCADE, null=False, verbose_name='Товар')
    count = models.PositiveSmallIntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'корзину'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя: {self.user}'
