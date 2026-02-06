from django.urls import path
from apps.users.views import userview 
from apps.users.views import Roleview
from apps.users.views import UserRoleMappingView 
from apps.users.views import LinksView
from apps.users.views import RoleLinkMappingView
from apps.users.views import RoleDepartimentMappingView


urlpatterns = [
    path('login/',userview.UserLoginView.as_view(),name='login'),
    path('refresh/',userview.MytokenRefreshView.as_view(),name='refresh'),
    path('profile/',userview.getUserprofile.as_view(),name='profile'),
    
    path('register/',userview.UserCreateView.as_view(),name='register'),
    path('list-user/',userview.GetUsermaster.as_view(),name='get-all-user'),
    path('get-user-id/<int:user_id>',userview.GetUsermasterById.as_view(),name='get-user-by-id'),
    path('update-user/<int:user_id>',userview.UpdateUserView.as_view(),name='update-user'),
    
    path('role-create/',Roleview.RoleCreateView.as_view(),name='role-create'),
    path('list-role/',Roleview.ListRoleView.as_view(),name='get-all-role'),
    path('role-update/<int:role_id>',Roleview.UpdateRoleView.as_view(),name='role-update'),
    path('delete-role/<int:role_id>',Roleview.DeleteRoleView.as_view(),name='delete-role'),
    
    path('user-role-mapping/',UserRoleMappingView.CreateUserRoleMappingView.as_view(),name='user-role-mapping'),
    path('show/user-role-mapping/',UserRoleMappingView.ListUserRoleMappingVeiw.as_view(),name='user-role-mapping'),
    path('updated-user-role-master/<int:user_role_id>', UserRoleMappingView.UpdatedUserRoleMapping.as_view(),name='update-user-role'),
    path('get-user-role-master/<int:user_role_id>', UserRoleMappingView.GetByIdUserRoleMapping.as_view(),name='update-user-role'),
    
    path('create-links/',LinksView.CreateLinkView.as_view(),name='create-links'),
    path('list-links/',LinksView.ListLinksView.as_view(),name='create-links'),
    path('delete-links/<int:link_id>',LinksView.DeleteLinkview.as_view(),name='create-links'),
    
    
    path('role-link-mapping/',RoleLinkMappingView.CreateRoleLinkMapping.as_view(),name='role-link-mapping'),
    path('list-link-mapping/',RoleLinkMappingView.ListRoleLinkMapping.as_view(),name='role-link-mapping'),
    
    
    
    
    
    path('create/role-departiment-mapping/',RoleDepartimentMappingView.CreateRoleDepartimentMapping.as_view(),name='role-link-mapping'),
    
           
]


