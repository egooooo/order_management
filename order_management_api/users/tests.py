from rest_framework.test import APIRequestFactory, APITestCase, \
    force_authenticate

from django.contrib.auth.models import User
from users.models import UserProfile, UserRole
from users.views import UserProfileViewSet, UserRoleViewSet


class TestUserProfileViewSet(APITestCase):
    # TODO
    def setUp(self):
        pass


class TestUserRoleViewSet(APITestCase):
    # TODO
    def setUp(self):
        pass
