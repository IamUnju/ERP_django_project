from rest_framework import serializers
from apps.products.models.Product import ProductMaster

class ProductMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaster
        fields= ['product_id','product_name'
                 ,'description','sub_category_id',
                 'main_category_id','packing_type',
                 'no_pcs_per_pack','pcs',
                 'weight_per_pack','weight_per_piece']
