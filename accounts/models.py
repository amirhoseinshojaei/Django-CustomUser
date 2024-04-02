from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,name,last_name,age,gender,password=None,**extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        elif not name:
            raise ValueError('the name field must be set')
        elif not last_name:
            raise ValueError('the lat name field must be set')
        elif not age:
            raise ValueError('Please Enter your age')
        elif age<18:
            raise ValueError('your age must be grate than 17')
        elif not gender:
            raise  ValueError('Please Enter gender')
        elif not password:
            raise ValueError('Please Enter password')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, last_name=last_name, age=age, gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,last_name,age,gender,password=None,**extra_fields):
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
    age = models.CharField(max_length=10,choices=Gender_Type)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']     # description = A list of the field names that will be prompted for when creating a user via the createsuperuser management command. The user will be prompted to supply a value for each of these fields.

    def __str__(self):
        return f'User is {self.email}'
