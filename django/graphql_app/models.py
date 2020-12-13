from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):

    class Meta:
        db_table = "user"
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー"

    is_active = models.BooleanField(default=True, verbose_name="アクティブフラグ")
    is_staff = models.BooleanField(default=False, verbose_name="システム管理者フラグ")
    email = models.EmailField(
        null=False, max_length=255, unique=True, verbose_name="メールアドレス")
    tel_number = models.CharField(
        null=True, max_length=255, verbose_name="電話番号")
    name = models.CharField(null=True, max_length=100, verbose_name="名前")
    name_kana = models.CharField(
        null=True, max_length=200, verbose_name="フリガナ")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    # これが何をしているか分からんが、これがないと管理画面でログインができなくなる
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
