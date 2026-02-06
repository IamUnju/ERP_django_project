from apps.users.serializers import UserRoleMappingSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import UserRoleMapping


class  CreateUserRoleMappingView(generics.ListCreateAPIView):
    queryset = UserRoleMapping.UserRoleMappingMaster.objects.all()
    serializer_class = UserRoleMappingSerializer.UserRoleMappingSerializer
    
    
class ListUserRoleMappingVeiw(generics.ListAPIView):
    queryset = UserRoleMapping.UserRoleMappingMaster.objects.all()
    serializer_class = UserRoleMappingSerializer.UserRoleMappingListsSerializer
    
    
class UpdatedUserRoleMapping(generics.UpdateAPIView):
    queryset = UserRoleMapping.UserRoleMappingMaster.objects.all()
    serializer_class = UserRoleMappingSerializer.UserRoleMappingSerializer
    lookup_field='user_role_id'
    
class GetByIdUserRoleMapping(generics.RetrieveAPIView):
    queryset = UserRoleMapping.UserRoleMappingMaster.objects.all()
    serializer_class = UserRoleMappingSerializer.UserRoleMappingSerializer
    lookup_field='user_role_id'    