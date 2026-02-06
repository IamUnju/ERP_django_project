from apps.users.models.Links import LinksMaster
from apps.users.models.RoleLinkMapping import RoleLinksMappingMaster
from rest_framework import serializers
from rest_framework.response import Response


class RoleLinkMappingMasterSerializer(serializers.ModelSerializer):
    createdBy = serializers.CharField(read_only=True)
    createdAt = serializers.CharField(read_only=True)
    updatedBy = serializers.CharField(read_only=True)
    updatedAt = serializers.CharField(read_only=True)
    
    class Meta:
        model = RoleLinksMappingMaster
        fields = ['role_link_id','role_id','link_id','createdBy','updatedBy','createdAt','updatedAt']
    
    
    def validate(self,attrs):
        role_id = attrs.get('role_id')
        link_id = attrs.get('link_id')
        mapping = RoleLinksMappingMaster.objects.filter(role_id=role_id,link_id=link_id).exists()
        if mapping:
            return Response({
                "detail":"role link mapping is already exists"
            })
        return attrs    
    
    def create(self,validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['createdBy']=request.user
        else:
            validated_data['createdBy']='ngoe'
        return super().create(validated_data)    
               
        
            
        
    