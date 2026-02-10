from rest_framework import serializers
from apps.products.models.ProductGrnModel import ProductsGRN_hdr, ProductsGRN_dtl
from datetime import timezone

#  sno = models.AutoField(primary_key=True)
#     grn_ref_no = models.CharField(unique=True,max_length=50)
#     grn_date = models.DateField(default=datetime.now)
#     grn_source = models.CharField(max_length=50,null=True,blank=True)
#     delivery_ref_no = models.CharField(max_length=50,null=True,blank=True)
#     source_store_id = models.IntegerField(null=True,blank=True)
#     grn_store_id = models.IntegerField(null=True,blank=True)
#     supplier_id = models.IntegerField(null=True,blank=True)
#     supplier_invoice_no = models.CharField(null=True,blank=True)
#     purchase_no = models.CharField(null=True,blank=True)
#     driver_name = models.CharField(null=True,blank=True)
#     driver_contacts = models.CharField(null=True,blank=True)
#     vehicle_no = models.CharField(null=True,blank=True)
#     seal_no = models.CharField(null=True,blank=True)
#     created_by = models.CharField(null=True,blank=True)
#     created_date = models.DateTimeField(auto_now=True)
#     modified_by = models.CharField(null=True,blank=True)
#     modified_date = models.DateTimeField(auto_now_add=True)




class ProductsGRN_hdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsGRN_hdr
        fields = ['grn_ref_no','grn_date','grn_source','delivery_ref_no','source_store_id','grn_store_id','supplier_id','supplier_invoice_no','purchase_no','driver_name','driver_contacts','vehicle_no','seal_no']
        
    def create(self, validated_data):
        data = validated_data
        print(data)
        # grn = validated_data.pop('grn_ref_no')
        # if not grn:
        #     year = timezone.now().year
        #     last_grn = ProductsGRN_hdr.objects.filter(grn_ref_no__startswith=f"GRN-{year}").order_by("sno").last()
            
        #     if last_grn:
        #         last_number = int(last_grn.grn.split("-")[-1])
        #         new_number = last_number+1
        #         data['grn_ref_no']=f"GRN-{year}-{new_number}"
        #     else:
        #         new_number = 1    
            
        #     data['grn_ref_no']=f"GRN-{year}-{new_number}"
        #     print(data)
        return super().create(data)    
        
        
        
        
# class ProductsGRN_dtlSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductsGRN_dtl
#         fields = ['grn_ref_no','main_category_id','sub_category_id','product_id','total_packing','packing_type','no_pcs_per_packing','total_pcs','remarks','status_entry','stock_pcs','order_no','packed_kg','lot_dtl_no','bar_code_ref_no','rate_per_pcs','total_product_price','currency']        