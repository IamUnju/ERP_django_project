from apps.users.serializers import LinkSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from apps.users.models import Links
from apps.users.serializers import LinkSerializer
from apps.users.permission import auth_permissoin
class CreateLinkView(generics.ListCreateAPIView):
    queryset = Links.LinksMaster.objects.all()
    serializer_class = LinkSerializer.LinksMasterSerializer

class ListLinksView(generics.ListAPIView):
    queryset = Links.LinksMaster.objects.all()
    serializer_class = LinkSerializer.LinksMasterSerializer
    # permission_classes = [auth_permissoin]
    
class DeleteLinkview(generics.DestroyAPIView):
    queryset = Links.LinksMaster.objects.all()
    serializer_class = LinkSerializer.LinksMasterSerializer
    lookup_field = 'link_id'    
    

        
    
   
    
    
             
    