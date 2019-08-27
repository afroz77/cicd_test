from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):

    def create_user(self, email, username, password):
        user_obj = None
        try:
            user_obj = self.model(email=self.normalize_email(email), username=username)
            user_obj.set_password(password)
            user_obj.save(using=self._db)
        except Exception as e:
            print("Exception Error", str(e))
        return user_obj

    def create_superuser(self, email, username, password):
        user_obj = None
        try:
            user_obj = self.model(email=self.normalize_email(email), username=username)
            user_obj.set_password(password)
            user_obj.is_staff = True
            user_obj.is_active = True
            user_obj.admin = True
            user_obj.is_superuser = True,
            user_obj.save(using=self._db)
        except Exception as e:
            print("Exception Error", str(e))
        return user_obj


class Account(AbstractBaseUser):

    first_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    email = models.EmailField(verbose_name='Email Address', max_length=255, unique=True)
    username = models.CharField(default=None, max_length=255)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def save(self, *args, **kwargs):
        li = []
        for i in args:
            li.append(i)
        print(li)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin