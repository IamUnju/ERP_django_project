from rest_framework import generics 
from rest_framework.response import Response
from rest_framework import status

from apps.products.models.ProductGrnModel import ProductsGRN_hdr
from apps.products.serializers.ProductGRNserializer import ProductsGRN_hdrSerializer



class CreateProductGRN_hdr(generics.ListCreateAPIView):
    queryset = ProductsGRN_hdr.objects.all()
    serializer_class = ProductsGRN_hdrSerializer