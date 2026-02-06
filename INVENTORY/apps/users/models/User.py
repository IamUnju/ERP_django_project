from django.contrib.auth.hashers import check_password, make_password
from django.db import models
from apps.users.models.Departimant import DepartimentMaster
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin


class UserMasterManager(BaseUserManager):
    def create_user(self,username,email,password=None,**extra_kwargs):
        if not username:
            raise ValueError('username is required')       
        if not email:
            raise ValueError('email is required')
        
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,**extra_kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,email,password=None,**extra_kwargs):
        extra_kwargs.setdefault('is_staff',True)
        extra_kwargs.setdefault('is_superuser',True)
        return self.create_user(username,email,password,**extra_kwargs)
            

class UserMaster(AbstractBaseUser,PermissionsMixin):
    objects = UserMasterManager()
    STATUS_CHOICES = (
        ('ACTIVE','ACTIVE'),
        ('INACTIVE','INACTIVE')
    )
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    department_id = models.ForeignKey(DepartimentMaster, on_delete=models.SET_NULL, related_name='users', null=True,blank=True)
    user_status = models.CharField(max_length=200,choices=STATUS_CHOICES,default='ACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=['email']
      
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)  
    
    def __str__(self):
        return self.username
    
    

