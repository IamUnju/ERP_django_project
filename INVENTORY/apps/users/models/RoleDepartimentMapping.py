from django.db import models
from apps.users.models import Departimant
from apps.users.models import Role


class RoleDepartimentMappingMaster(models.Model):
    role_departiment_id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey(Role.RoleMaster, on_delete=models.SET_NULL, null=True,blank=True)
    departiment_id = models.ForeignKey(Departimant.DepartimentMaster,on_delete=models.SET_NULL,null=True,blank=True)
    createdBy = models.CharField(max_length=50, null=True)
    updatedBy = models.CharField(max_length=50, null=True)
    createdAt = models.DateTimeField( auto_now_add=True)
    updatedAt = models.DateTimeField( auto_now=True)