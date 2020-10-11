from rest_framework import serializers

from users.models import UserProfile, UserRole


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'created', 'name', 'email', 'role']

    name = serializers.SerializerMethodField(source='get_name')

    def get_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'


class UserProfileRetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'created', 'first_name', 'last_name', 'email', 'role']


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id', 'name', 'slug', 'is_admin']
