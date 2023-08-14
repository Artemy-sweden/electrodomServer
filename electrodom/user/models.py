from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

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
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(upload_to='users_photos', blank=True)
    phone_number = models.CharField(max_length=13, blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(unique=True)

    # Убираем поле username и указываем email как уникальное поле аутентификации
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email




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

    # def save(self, *args, **kwargs):
    #     existing_basket = Basket.objects.filter(user=self.user, goods=self.goods).first()
    #
    #     if existing_basket:
    #         existing_basket.count += self.count
    #         existing_basket.save()
    #     else:
    #         super(Basket, self).save(args, **kwargs)
