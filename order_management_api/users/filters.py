from django_filters import rest_framework as filters
from django.db.models import Q

from users.models import UserProfile, UserRole


class UserProfileFilter(filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'email']
        order_by = model()._meta.ordering

    order = filters.OrderingFilter(
        fields=['id', 'created', 'email', 'first_name', 'last_name']
    )


class UserRoleFilter(filters.FilterSet):
    class Meta:
        model = UserRole
        fields = ['id', 'name', 'slug', 'is_admin']
        order_by = model()._meta.ordering

    order = filters.OrderingFilter(
        fields=['id', 'name', 'slug', 'is_admin']
    )
