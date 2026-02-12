from rest_framework import serializers
from apps.products.models.ProductGrnModel import ProductsGRN_hdr, ProductsGRN_dtl
from datetime import timezone
from datetime import datetime
from apps.products.services.ProductGRNservice import Reference_number



class ProductsGRN_hdrSerializer(serializers.ModelSerializer):
    grn_ref_no = serializers.CharField(read_only=True)
    class Meta:
        model = ProductsGRN_hdr
        fields = ['grn_ref_no','grn_date','grn_source','delivery_ref_no','source_store_id','grn_store_id','supplier_id','supplier_invoice_no','purchase_no','driver_name','driver_contacts','vehicle_no','seal_no']
                               
    def create(self, validated_data):
        data = validated_data
        grn = validated_data.get('grn_ref_no')
        if not grn:
            ref_no=Reference_number.Reference_no_generator(grn)
            print("hapo tena",ref_no)
            if ref_no:
                data['grn_ref_no'] = ref_no 
        return super().create(data)    
    
    
    
    
    
    
        
        
          
        
class ProductsGRN_dtlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsGRN_dtl
        fields = ['grn_ref_no','main_category_id','sub_category_id','product_id','total_packing','packing_type','no_pcs_per_packing','total_pcs','remarks','status_entry','stock_pcs','order_no','packed_kg','lot_dtl_no','bar_code_ref_no','rate_per_pcs','total_product_price','currency']        