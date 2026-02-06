from django.db import models
from apps.products.models.SubCategory import SubCategoryMaster
from apps.products.models.MainCategory import MainCategoryMaster
class ProductMaster(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=120,unique=True)
    description = models.CharField(max_length=130)
    sub_category_id = models.ForeignKey(SubCategoryMaster,on_delete=models.SET_NULL,null=True,blank=True )
    main_category_id = models.ForeignKey(MainCategoryMaster,on_delete=models.SET_NULL,null=True,blank=True )
    packing_type = models.CharField(max_length=50,null=True,blank=True)
    no_pcs_per_pack = models.IntegerField(null=True,blank=True)
    pcs = models.IntegerField(null=True,blank=True)
    weight_per_pack = models.FloatField(null=True,blank=True)
    weight_per_piece = models.FloatField(null=True,blank=True)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
       
    def __str__(self):
        return self.product_name