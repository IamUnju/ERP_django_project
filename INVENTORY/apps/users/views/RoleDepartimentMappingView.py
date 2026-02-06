from rest_framework import generics
from apps.users.serializers.RoleDepartimentMapping import RoleDepartimentMappingMasterSerializer
from apps.users.models.RoleDepartimentMapping import RoleDepartimentMappingMaster

class CreateRoleDepartimentMapping(generics.ListCreateAPIView):
    queryset = RoleDepartimentMappingMaster.objects.all()
    serializer_class = RoleDepartimentMappingMasterSerializer