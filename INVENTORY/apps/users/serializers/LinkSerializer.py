from rest_framework import serializers
from apps.users.models import Links

class LinksMasterSerializer(serializers.ModelSerializer):
    createdBy = serializers.CharField(read_only=True)
    updatedBy = serializers.CharField(read_only=True)
    createdAt = serializers.CharField(read_only=True)
    updatedAt = serializers.CharField(read_only=True)
  
    class Meta:
        model = Links.LinksMaster
        fields = ['link_id','link_name','link_url','createdBy','updatedBy','createdAt','updatedAt']
        
        
    def validate(self,attrs):
        link_name = attrs.get('link_name')
        link_url = attrs.get('link_url')
        link = Links.LinksMaster.objects.filter(link_url=link_url).exists()
        if link:
            raise serializers.ValidationError({
                "error":"link name or link url is already exists"
            })
            
        return attrs    
        
        
    def create(self,validated_data):      
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['createdBy']=request.user
        else:
            validated_data['createdBy']='ngoe'           
        return super().create(validated_data) 
    
    
    def upadate(self,instance,validated_data):
        request = request.context.get('request')
        if request and request.user.is_authenticated:
            validated_data.get('updatedBy')
        else:
            validated_data['updatedBy']='ngoe'            
        return super().update(instance,validated_data)         
    
     
