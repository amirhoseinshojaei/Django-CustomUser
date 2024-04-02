from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager,PermissionsMixin
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
