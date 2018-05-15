from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class TestUserManager(BaseUserManager):

    def create_user(self, username, password=None, mobile_no='9988776655', email=None):

        if not username:
            raise ValueError('Users must have an username')
        import pdb;pdb.set_trace()
        user = self.model(
            username=username,
            mobile_no=mobile_no,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, mobile_no, name=None, email=None):
        user = self.create_user(username, password=password, mobile_no=mobile_no, email=email)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    #name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    mobile_no = models.CharField(max_length=12)
    is_staff = models.BooleanField(('user status'), default=False,)
    is_superuser = models.BooleanField(('staff status'),default=False)

    objects = TestUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['mobile_no', 'email']


class Todo(models.Model):
    todo_text = models.CharField(max_length=50, null=True, blank=True)
    checked = models.BooleanField(default=False)
    creator = models.ForeignKey(UserProfile, related_name='todos', null=True, on_delete=models.CASCADE)
    created_at = models.DateField(timezone.now(), null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=128, null=True, blank=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        ordering = ('created_at',)

    def count(self):
        return self.count()

    def count_finished(self):
        return self.filter(is_finished=True).count()

    def count_open(self):
        return self.filter(is_finished=False).count()


class Registration(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
