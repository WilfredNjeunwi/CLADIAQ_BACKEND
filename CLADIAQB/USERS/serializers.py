from rest_framework import serializers
from .models import CustomUser, Organization, UserOrganizationRole

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'address', 'tell_num', 'profileID', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class UserOrganizationRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrganizationRole
        fields = '__all__'