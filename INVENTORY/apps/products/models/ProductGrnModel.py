from django.db import models
from datetime import datetime

class ProductsGRN_hdr(models.Model):
    sno = models.AutoField(primary_key=True)
    grn_ref_no = models.CharField(unique=True,max_length=50)
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
        



# class ProductsGRN_dtl(models.Model):
#     USE [Store]
# GO

# SELECT [Sno]
#       ,[GRN_Ref_No]
#       ,[Main_Category_Id]
#       ,[Sub_Category_Id]
#       ,[Product_Id]
#       ,[Total_Packing]
#       ,[Packing_Type]
#       ,[No_Pcs_Per_Packing]
#       ,[Total_Pcs]
#       ,[Remarks]
#       ,[Status_Entry]
#       ,[Created_By]
#       ,[Created_Date]
#       ,[Created_Mac_Address]
#       ,[Modified_By]
#       ,[Modified_Date]
#       ,[Modified_Mac_Address]
#       ,[Stock_Pcs]
#       ,[Order_No]
#       ,[Packed_KG]
#       ,[Lot_Dtl_No]
#       ,[Bar_Code_Ref_No]
#       ,[Rate_Per_Pcs]
#       ,[Total_Product_Price]
#       ,[Currency]
#       ,[Exchange_Rate]
#       ,[Expiry_Date]
#       ,[PO_Ref_NO]
#       ,[RACK_ID]
#       ,[Alternate_Packing_Type]
#       ,[Truck_Id]
#       ,[SECTION_ID]
#       ,[MACHINE_ID]
#       ,[PALLET_ID]
#       ,[PURCHASE_BARCODE_REF_NO]
#       ,[Po_Number]
#       ,[Yard_Point]
#       ,[Product_Serial_No]
#       ,[Container_No]
#   FROM [StoEntries].[tbl_Goods_Inward_GRN_Dtl]

# GO



        
    
    
    
    
    
    
    