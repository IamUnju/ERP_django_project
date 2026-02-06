from apps.products.models.SubCategory import SubCategoryMaster
from rest_framework import serializers

    # sub_category_id = models.AutoField(primary_key=True)
    # main_category_id = models.ForeignKey(MainCategoryMaster,on_delete=models.SET_NULL,null=True,blank=True )
    # sub_category_name = models.CharField(max_length=120,unique=True)
    # description = models.CharField(max_length=130)
    # created_by = models.CharField(max_length=50)
    # created_at = models.DateTimeField(auto_now=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

class SubCategoryMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryMaster
        fields = ['sub_category_id','main_category_id','sub_category_name','description']
        
        
    def validate(self, attrs):
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        
        return super().update(instance, validated_data)