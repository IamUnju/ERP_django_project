from rest_framework import serializers
from apps.users.models import Role



class RoleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role.RoleMaster
        fields = ['role_id','role_name','role_desc']


class RoleMasterSerializer(serializers.ModelSerializer):
    
    createdBy = serializers.StringRelatedField(read_only=True)
    updatedBy = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Role.RoleMaster
        fields = ['role_id','role_name','role_desc','createdBy','updatedBy','createdAt','updatedAt']
        
    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request,'user'):
            validated_data['createdBy'] = request.user
        return super().create(validated_data)        


    def update(self, instance, validated_data):
        request = self.context.get('request')
        if request and hasattr(request,'user'):
            validated_data['updatedBy'] = request.user
        return super().update(instance, validated_data)
    
  
