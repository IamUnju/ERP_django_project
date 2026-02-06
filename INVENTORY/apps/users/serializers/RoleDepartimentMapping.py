from apps.users.models.RoleDepartimentMapping import RoleDepartimentMappingMaster
from rest_framework import serializers

class RoleDepartimentMappingMasterSerializer(serializers.ModelSerializer):
    createdBy = serializers.CharField(read_only=True)
    createdAt = serializers.CharField(read_only=True)
    updatedBy = serializers.CharField(read_only=True)
    updatedAt = serializers.CharField(read_only=True)
    
    class Meta:
        model = RoleDepartimentMappingMaster
        fields = ['role_departiment_id','role_id','departiment_id','createdBy','updatedBy','createdAt','updatedAt']
    
  
    
    def validate(self,attrs):
        role_id = attrs.get('role_id')
        departiment_id = attrs.get('departiment_id')
        mapping = RoleDepartimentMappingMaster.objects.filter(role_id=role_id,departiment_id=departiment_id).exists()
        if mapping:
            return({
                "detail":"role departiment mapping is already exists"
            })
        return attrs    
    
    def create(self,validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['createdBy']=request.user
        else:
            validated_data['createdBy']='ngoe'
        return super().create(validated_data)