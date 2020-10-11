from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

from config.utils import api_response
from config.views import BaseReadOnlyViewSet

from users.models import UserProfile, UserRole
from users.filters import UserProfileFilter, UserRoleFilter
from users.serializers import UserProfileSerializer, UserProfileRetSerializer,\
    UserRoleSerializer


class UserProfileViewSet(BaseReadOnlyViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserProfileFilter

    def list(self, request, *args, **kwargs):
        response = super(UserProfileViewSet, self).list(
            request, *args, **kwargs
        )
        return Response(api_response(data=response.data))

    def retrieve(self, request, user_id=None, *args, **kwargs):
        try:
            user = UserProfile.objects.get(id=self.kwargs.get('user_id'))
        except:
            # 150 - User not found
            return Response(
                api_response(status_code=150),
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UserProfileRetSerializer(user)
        return Response(api_response(data=serializer.data))


class UserRoleViewSet(BaseReadOnlyViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserRoleFilter

    def list(self, request, *args, **kwargs):
        # checking if the user is an administrator
        active_user = self.request.user
        up = UserProfile.objects.get(user_id=active_user.id)

        if up.role.is_admin is not True:
            # 201 - Only available for the administrator role
            return Response(
                api_response(status_code=201),
                status=status.HTTP_400_BAD_REQUEST
            )

        response = super(UserRoleViewSet, self).list(
            request, *args, **kwargs
        )
        return Response(api_response(data=response.data))
