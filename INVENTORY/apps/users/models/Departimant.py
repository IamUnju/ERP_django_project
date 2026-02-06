from django.db import models

class DepartimentMaster(models.Model):
    dept_id = models.AutoField(primary_key=True)
    departiment = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.departiment