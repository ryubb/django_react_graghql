from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class UserModel(AbstractBaseUser):

    class Meta:
        db_table = "user"
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー"

    is_active = models.BooleanField(default=True, verbose_name="アクティブフラグ")
    email = models.EmailField(
        null=False, max_length=255, unique=True, verbose_name="メールアドレス")
    tel_number = models.CharField(
        null=True, max_length=255, verbose_name="電話番号")
    name = models.CharField(null=True, max_length=100, verbose_name="名前")
    name_kana = models.CharField(
        null=True, max_length=200, verbose_name="フリガナ")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
