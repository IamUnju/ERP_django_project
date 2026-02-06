from rest_framework import generics
from apps.users.models.User import UserMaster

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.serializers.userserializer import UserLoginSerializer,UserMasterSerializer
from rest_framework.response import Response
from rest_framework import status
from apps.users.permission import auth_permissoin
from apps.users.serializers.TokenRefreshSerializer import MyTokenRefreshSerializer


class UserCreateView(generics.CreateAPIView):
    
    queryset = UserMaster.objects.all()
    serializer_class = UserMasterSerializer
    

    
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
        
    def post(self,request,*args,**kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        username = serializers.validated_data['username']
        password = serializers.validated_data['password']
        try:
            user = UserMaster.objects.get(username=username, user_status='ACTIVE')
        except UserMaster.DoesNotExist:
            return Response({'datails':'invalid credential user'},status=401)       
        if user.check_password(password): 
            
            print(f"password matched ${user.username}") 
                     
            Refresh = RefreshToken.for_user(user)
            return Response ({
                'access':str(Refresh.access_token),
                'refresh':str(Refresh),
                'user_id': user.user_id,
                'username': user.username                           
            })            
        return Response({'detailed','invalid credentials password check'},status=status.HTTP_401_UNAUTHORIZED)    
     
     
class MytokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer
                
class getUserprofile(generics.GenericAPIView):
    def get(self,request):
        user = request.user
        print(user)
 
class UpdateUserView(generics.GenericAPIView):
    serializer_class = UserMasterSerializer
    queryset = UserMaster.objects.all()
    lookup_field= 'user_id'
             
    def put(self,request,*args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
        

class GetUsermaster(generics.ListAPIView):
    queryset = UserMaster.objects.all()
    serializer_class = UserMasterSerializer
    permission_classes = [auth_permissoin]

    

class GetUsermasterById(generics.RetrieveAPIView):
    queryset = UserMaster.objects.all()
    serializer_class = UserMasterSerializer
    lookup_field='user_id'

    
    
class DeleteUsermaster(generics.DestroyAPIView):
    queryset = UserMaster.objects.all()
    serializer_class = UserMasterSerializer
    lookup_field = 'user_id'      
         
     
                    
            
        
        
    
