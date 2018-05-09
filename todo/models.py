from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser )
from django.contrib.auth.models import PermissionsMixin




class MyUserManager(BaseUserManager):
    def create_user(self,email,password=None, mobile_no=None,name=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            mobile_no=mobile_no,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,name,mobile_no):
        user=self.create_user(
        email,
        password=password,name=name,mobile_no=mobile_no
    )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    mobile_no = models.IntegerField()

    is_staff = models.BooleanField(('staff status'), default=False,)
    is_superuser = models.BooleanField(('staff status'),default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile_no']


class Todo(models.Model):
    text = models.CharField(max_length=50, null=True, blank=True)
    checked = models.BooleanField(default=False)
    creator = models.ForeignKey(UserProfile, related_name='todos', null=True, on_delete=models.CASCADE)
    created_at = models.DateField(null=True, blank=True)
    finished_at = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.task_name

    def __str__(self):
        return self.text

    def count(self):
        return self.todos.count()

    def count_finished(self):
        return self.todos.filter(is_finished=True).count()

    def count_open(self):
        return self.todos.filter(is_finished=False).count()
