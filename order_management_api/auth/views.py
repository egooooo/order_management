from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework import status
from rest_framework.response import Response
from django.contrib import auth
from django.contrib.auth.models import User

from config.settings import SECRET_KEY
from config.utils import api_response
from config.views import BaseExternalView, BaseView

from users.models import UserProfile, UserRole

import jwt


class RegistrationView(BaseView):
    def post(self, request):
        data = request.data

        active_user = self.request.user
        up = UserProfile.objects.get(user_id=active_user.id)

        # checking if the user is an administrator
        if up.role.is_admin is not True:
            # 151 - Only admin can create users
            return Response(
                api_response(status_code=151),
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user_role = UserRole.objects.get(id=data.get('role_id'))
        except:
            # 200 - Role not found
            return Response(
                api_response(status_code=200),
                status=status.HTTP_400_BAD_REQUEST
            )

        if data.get('password_first') != data.get('password_second'):
            # 151 - Password does not match
            return Response(
                api_response(status_code=151),
                status=status.HTTP_400_BAD_REQUEST
            )

        # create auth_user
        auth_user = User.objects.create_user(
            username=data.get('email'),
            email=data.get('email'),
            password=data.get('password_first')
        )

        if not auth_user:
            # 999 - Unhandled exception
            return Response(
                api_response(status_code=999),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        try:
            # create user profile
            user = UserProfile()
            user.first_name = data.get('first_name')
            user.last_name = data.get('last_name')
            user.email = data.get('email')
            user.role_id = user_role.id
            user.user_id = auth_user.id
            user.save()

            return Response(api_response(data=user.id))

        except:
            User.objects.get(id=auth_user.id).delete()
            # 100 - Wrong input data
            return Response(
                api_response(status_code=100),
                status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(BaseExternalView):
    def post(self, request):
        data = request.data

        try:
            up = UserProfile.objects.get(email=data.get('login'))
        except:
            # 150 - User not found
            return Response(
                api_response(status_code=150),
                status=status.HTTP_400_BAD_REQUEST
            )

        auth_user = auth.authenticate(
            username=data.get('login'),
            password=data.get('password')
        )

        if auth_user is None:
            # 108 - Incorrect password
            return Response(
                api_response(status_code=108),
                status=status.HTTP_400_BAD_REQUEST
            )

        payload = jwt_payload_handler(up.user)
        token = jwt.encode(payload, SECRET_KEY)

        result = dict()
        result['id'] = up.id
        result['name'] = f"{up.first_name} {up.last_name}"
        result['email'] = up.email
        result['role'] = up.role.slug
        result['access_token'] = token

        return Response(api_response(data=result))
