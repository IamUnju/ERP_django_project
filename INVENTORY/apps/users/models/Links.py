from django.db import models

class LinksMaster(models.Model):
    link_id = models.AutoField(primary_key=True)
    link_name = models.CharField(max_length=100,null=True,blank=True)
    link_url = models.CharField(max_length=200,null=True,blank=True)
    createdBy = models.CharField(max_length=50,null=True,blank=True)
    updatedBy = models.CharField(max_length=100,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.link_name