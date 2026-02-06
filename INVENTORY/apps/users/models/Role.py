from django.db import models
from apps.users.models.User import UserMaster


status_choice = (('ACTIVE','ACTIVE'),('INACTIVE','INACTIVE'))

class RoleMaster(models.Model):
       
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50,unique=True)
    role_desc = models.CharField(max_length=150,null=True,blank=True)
    role_status = models.CharField(max_length=50,choices=status_choice,default='ACTIVE')
    createdBy = models.CharField(max_length=100,null=True,blank=True)
    updatedBy = models.CharField(max_length=100,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
       
    def __str__(self):
        return self.role_name
    


    

    

    