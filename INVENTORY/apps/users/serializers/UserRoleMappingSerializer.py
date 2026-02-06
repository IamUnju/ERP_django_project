from rest_framework import serializers
from apps.users.models import UserRoleMapping

class UserRoleMappingSerializer(serializers.ModelSerializer):
    createdBy = serializers.StringRelatedField(read_only=True)
    updatedBy = serializers.StringRelatedField(read_only=True)
    createdAt = serializers.DateTimeField(read_only=True)
    updatedAt = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = UserRoleMapping.UserRoleMappingMaster
        fields = ['user_role_id','role_id','user_id','createdBy','updatedBy','createdAt','updatedAt']
       
    def create(self,validated_data):
        request = self.context.get('request')
        if request and hasattr(request,'user'):
            validated_data['createdBy']=request.user
        return super().create(validated_data)          
          
    def update(self,instance,validated_data):
        request = request.context.get('request')
        if request and hasattr(request,'user'):
            validated_data['updatedBy']=request.user
        return super().update(instance,validated_data)            
        
class UserRoleMappingListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoleMapping.UserRoleMappingMaster
        fields = ['user_role_id','role_id','user_id']         