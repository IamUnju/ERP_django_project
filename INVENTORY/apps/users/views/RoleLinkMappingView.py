from rest_framework import generics
from apps.users.serializers.RoleLinkMappingSerializer import RoleLinkMappingMasterSerializer
from apps.users.models.RoleLinkMapping import RoleLinksMappingMaster 


class CreateRoleLinkMapping(generics.ListCreateAPIView):
    queryset = RoleLinksMappingMaster.objects.all()
    serializer_class = RoleLinkMappingMasterSerializer
    
class ListRoleLinkMapping(generics.ListAPIView):
   queryset = RoleLinksMappingMaster.objects.all()
   serializer_class = RoleLinkMappingMasterSerializer