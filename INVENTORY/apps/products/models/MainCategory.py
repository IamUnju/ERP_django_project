from django.db import models

class MainCategoryMaster(models.Model):
    main_category_id = models.AutoField(primary_key=True)
    main_category_name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=130)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.main_category_name
    
    