from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from apps.users.models import RoleLinkMapping
from apps.users.models import UserRoleMapping


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    
    def validate(self,attrs):
        data = super().validate(attrs)
        if data:
            refreshToken = attrs.get('refresh') 
            refresh = self.token_class(refreshToken)
            user_id = refresh.get('user_id')
            # print(user_id)
            # username = refresh.get('username')   
            roles_rq = UserRoleMapping.UserRoleMappingMaster.objects.filter(user_id=user_id).select_related('role_id')          
            role_id = roles_rq.values_list('role_id',flat=True)
            role_name = roles_rq.values_list('role_id__role_name',flat=True)
            links = RoleLinkMapping.RoleLinksMappingMaster.objects.filter(role_id__in=role_id).values_list('link_id__link_url',flat=True)      
            data['roles']=list(role_name)
            data['permitted_links']=list(links)        
            return data
            
            
            
            
            

