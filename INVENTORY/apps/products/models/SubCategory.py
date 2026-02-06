from django.db import models
from apps.products.models.MainCategory import MainCategoryMaster

class SubCategoryMaster(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    main_category_id = models.ForeignKey(MainCategoryMaster,on_delete=models.SET_NULL,null=True,blank=True )
    sub_category_name = models.CharField(max_length=120,unique=True)
    description = models.CharField(max_length=130)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
       
    def __str__(self):
        return self.sub_category_name
    
    