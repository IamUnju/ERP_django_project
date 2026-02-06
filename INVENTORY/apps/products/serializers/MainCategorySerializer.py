from rest_framework import serializers
from apps.products.models.MainCategory import MainCategoryMaster


class MainCategoryMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategoryMaster
        fields = ['main_category_id','main_category_name','description']
        
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        
        return super().update(instance, validated_data)    