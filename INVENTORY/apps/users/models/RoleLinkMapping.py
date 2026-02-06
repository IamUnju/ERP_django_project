from django.db import models
from apps.users.models import Role
from apps.users.models import Links


class RoleLinksMappingMaster(models.Model):
    role_link_id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey(Role.RoleMaster, on_delete=models.SET_NULL, null=True,blank=True)
    link_id = models.ForeignKey(Links.LinksMaster,on_delete=models.SET_NULL,null=True,blank=True)
    createdBy = models.CharField(max_length=50, null=True)
    updatedBy = models.CharField(max_length=50, null=True)
    createdAt = models.DateTimeField( auto_now_add=True)
    updatedAt = models.DateTimeField( auto_now=True)
    
     
    
        