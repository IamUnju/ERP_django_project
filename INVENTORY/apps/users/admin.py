from django.contrib import admin
from apps.users.models import User 
from apps.users.models import Role
admin.site.register(User.UserMaster)
admin.site.register(User.DepartimentMaster)
admin.site.register(Role.RoleMaster) 