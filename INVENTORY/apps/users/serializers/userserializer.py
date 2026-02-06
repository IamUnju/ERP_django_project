from rest_framework import serializers
from apps.users.models.User import UserMaster
from apps.users.models.Departimant import DepartimentMaster



class UserMasterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # department = serializers.CharField(source='Departimant.DepartimentMaster',read_only=True)
    class Meta:
        model = UserMaster
        fields = ['user_id', 'username', 'email','password', 'department_id', 'user_status']
                
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserMaster.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password',None)
        for key,value in validated_data.items():
            setattr(instance, key, value)
        if password:
            instance.set_password(password)
            instance.save()
        return instance    
            
                                
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
