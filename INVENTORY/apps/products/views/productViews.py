from rest_framework.response import Response
from rest_framework import generics
from apps.products.models.MainCategory import MainCategoryMaster
from apps.products.models.SubCategory import SubCategoryMaster
from apps.products.serializers.SubCategorySerializer import SubCategoryMasterSerializer

from apps.products.serializers.MainCategorySerializer import MainCategoryMasterSerializer

class CreateMainCategory(generics.ListCreateAPIView):
    queryset = MainCategoryMaster.objects.all()
    serializer_class = MainCategoryMasterSerializer
    
    
class CreateSubCategory(generics.ListCreateAPIView):
    queryset = SubCategoryMaster.objects.all()
    serializer_class = SubCategoryMasterSerializer    
      

