from rest_framework.permissions import BasePermission
from apps.users.models.UserRoleMapping import UserRoleMappingMaster
from apps.users.models.RoleLinkMapping import RoleLinksMappingMaster
from apps.users.models.Links import LinksMaster


class auth_permissoin(BasePermission):
    
    def has_permission(self, request, view):
        
        public_urls = ['/api/login/','/api/register/']
        
        if request.path in public_urls:
            return True
        
        
        if not request.user or not request.user.is_authenticated:
            return False
        
        
        user = request.user
        # print(user.user_id)
        
        
        roles = UserRoleMappingMaster.objects.filter(user_id = user.user_id).values_list('role_id',flat=True)
        
        # print(roles)

        
        if not LinksMaster.objects.filter(link_url=request.path).exists():
            return False
        
        
        if not roles.exists():
            return False
        
        Allowed_links = RoleLinksMappingMaster.objects.filter(role_id__in=roles).values_list('link_id',flat=True).exists()
        print(Allowed_links)
        return Allowed_links
            
            
        
            
            
            
         
