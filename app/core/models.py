"""
Django Models
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.conf import settings

class UserManager(BaseUserManager):
    """Manager for user"""
    def create_user(self, email, password=None, **extra_field):
        """Create,save and return a new user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """Create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # phone_no = models.IntegerF(unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Patient(models.Model):
    """Patient object"""
    patient_name = models.CharField(max_length=30)
    phone_no = models.IntegerField(unique=True)
    address = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()

    def __str__(self):
        return self.patient_name