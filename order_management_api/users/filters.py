from django_filters import rest_framework as filters
from django.db.models import Q

from users.models import UserProfile


class UserProfileFilter(filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'email']
        order_by = model()._meta.ordering

    order = filters.OrderingFilter(
        fields=['id', 'created', 'email', 'first_name', 'last_name']
    )
