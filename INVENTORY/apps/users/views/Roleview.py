from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from  apps.users.models.Role import RoleMaster
from apps.users.serializers.roleserializer import RoleMasterSerializer,RoleListSerializer


class RoleCreateView(generics.CreateAPIView):
    queryset = RoleMaster.objects.all()
    serializer_class = RoleMasterSerializer
    
class UpdateRoleView(generics.RetrieveUpdateAPIView):
        queryset = RoleMaster.objects.all()
        serializer_class = RoleMasterSerializer
        lookup_field= 'role_id'
        
          
class ListRoleView(generics.ListAPIView):
    queryset = RoleMaster.objects.all()
    serializer_class = RoleListSerializer
 
        
class GetRoleViewById(generics.RetrieveAPIView):
    queryset = RoleMaster.objects.all()
    serializer_class = RoleListSerializer
    lookup_field='role_id'        
    
class DeleteRoleView(generics.DestroyAPIView):
    queryset = RoleMaster.objects.all()
    serializer_class = RoleMasterSerializer
    lookup_field='role_id'    
    
    