from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,name,last_name,age,gender,password=None,**extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, last_name=last_name, age=age, gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,last_name,gender,age,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must have is_superuser=True')
        return self.create_user(email,name,last_name,age,gender,password=None,**extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    Gender_Type = (
        ('male','male'),
        ('female','female')
    )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=Gender_Type)
    age = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','last_name','age','gender']     # description = A list of the field names that will be prompted for when creating a user via the createsuperuser management command. The user will be prompted to supply a value for each of these fields.

    def __str__(self):
        return f'User is {self.email}'
