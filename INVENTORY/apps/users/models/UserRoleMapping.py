from django.db import models
from apps.users.models.Role import status_choice, RoleMaster
from apps.users.models.User import UserMaster

class UserRoleMappingMaster(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey(RoleMaster, on_delete=models.SET_NULL,null=True,blank=True)
    user_id = models.ForeignKey(UserMaster,on_delete=models.SET_NULL,null=True,blank=True)
    createdBy = models.CharField(max_length=50,null=True,blank=True)
    updatedBy = models.CharField(max_length=100,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user_role_id
    
    