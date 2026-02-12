from rest_framework import generics 
from rest_framework.response import Response
from rest_framework import status
from apps.products.models.ProductGrnModel import ProductsGRN_dtl
from apps.products.models.ProductGrnModel import ProductsGRN_hdr
from apps.products.serializers.ProductGRNserializer import ProductsGRN_hdrSerializer,ProductsGRN_dtlSerializer



class CreateProductGRN_hdr(generics.ListCreateAPIView):
    queryset = ProductsGRN_hdr.objects.all()
    serializer_class = ProductsGRN_hdrSerializer
    
    # def post(self,request,*args, **kwargs):    
    #     # data = request.data
    #     # ref_no = data.get('grn_ref_no')
    #     # print(ref_no)
    #     return Response(request)    
    #    ref_no = '34'
    # ref_no = Reference_number(ref_no)
    
    
class CreatedProductGRN_Details(generics.ListCreateAPIView):
    queryset = ProductsGRN_dtl.objects.all() 
    serializer_class = ProductsGRN_dtlSerializer    