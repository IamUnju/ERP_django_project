from django.db import models
from datetime import datetime
from django.utils import timezone
from apps.products.models.Product import ProductMaster
from apps.products.models.MainCategory import MainCategoryMaster
from apps.products.models.SubCategory import SubCategoryMaster

class ProductsGRN_hdr(models.Model):
    sno = models.AutoField(primary_key=True)
    grn_ref_no = models.CharField(unique=True,max_length=50,editable=True)
    grn_date = models.DateField(default=datetime.now)
    grn_source = models.CharField(max_length=50,null=True,blank=True)
    delivery_ref_no = models.CharField(max_length=50,null=True,blank=True)
    source_store_id = models.IntegerField(null=True,blank=True)
    grn_store_id = models.IntegerField(null=True,blank=True)
    supplier_id = models.IntegerField(null=True,blank=True)
    supplier_invoice_no = models.CharField(null=True,blank=True)
    purchase_no = models.CharField(null=True,blank=True)
    driver_name = models.CharField(null=True,blank=True)
    driver_contacts = models.CharField(null=True,blank=True)
    vehicle_no = models.CharField(null=True,blank=True)
    seal_no = models.CharField(null=True,blank=True)
    created_by = models.CharField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(null=True,blank=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    
    
        



class ProductsGRN_dtl(models.Model):
    sno = models.AutoField(primary_key=True)
    grn_ref_no = models.ForeignKey(ProductsGRN_hdr,on_delete=models.SET_NULL,null=True,blank=True)
    main_category_id = models.ForeignKey(MainCategoryMaster,on_delete=models.SET_NULL,null=True,blank=True)
    sub_category_id = models.ForeignKey(SubCategoryMaster,on_delete=models.SET_NULL,null=True,blank=True)
    product_id = models.ForeignKey(ProductMaster,on_delete=models.SET_NULL,null=True,blank=True)
    total_packing = models.IntegerField(null=True,blank=True)
    packing_type = models.CharField(max_length=50,null=True,blank=True)
    no_pcs_per_packing = models.IntegerField(null=True,blank=True)
    total_pcs = models.IntegerField(null=True,blank=True)
    remarks = models.CharField(max_length=200,null=True,blank=True)
    status_entry = models.CharField(max_length=50,null=True,blank=True)
    created_by = models.CharField(max_length=50,null=True,blank=True)
    created_date = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    stock_pcs = models.IntegerField(null=True,blank=True)
    order_no = models.CharField(max_length=50,null=True,blank=True)
    packed_kg = models.FloatField(null=True,blank=True)
    lot_dtl_no = models.CharField(max_length=50,null=True,blank=True)
    bar_code_ref_no = models.CharField(max_length=100,null=True,blank=True)
    rate_per_pcs = models.FloatField(null=True,blank=True)
    total_product_price = models.FloatField(null=True,blank=True)
    currency = models.CharField(max_length=20,null=True,blank=True)
    exchange_rate = models.FloatField(null=True,blank=True)
    expiry_date = models.DateField(null=True,blank=True)
    po_ref_no = models.CharField(max_length=50,null=True,blank=True)
    rack_id = models.CharField(max_length=50,null=True,blank=True)
    alternate_packing_type = models.CharField(max_length=50,null=True,blank=True)





        
    
    
    
    
    
    
    