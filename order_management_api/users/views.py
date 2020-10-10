from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

from config.utils import api_response
from config.views import BaseReadOnlyViewSet

from users.models import UserProfile
from users.filters import UserProfileFilter
from users.serializers import UserProfileSerializer, UserProfileRetSerializer


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
            user = UserProfile.objects.get(
                id=self.kwargs.get('user_id')
            )
        except:
            # 150 - User not found
            return Response(
                api_response(status_code=150),
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            serializer = UserProfileRetSerializer(user)
            return Response(api_response(data=serializer.data))

        except Exception as e:
            # 999 - Unhandled exception
            return Response(
                api_response(status_code=999, message=str(e)),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
