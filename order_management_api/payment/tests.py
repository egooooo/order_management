from rest_framework.test import APIRequestFactory, APITestCase, \
    force_authenticate

from django.contrib.auth.models import User
from payment.models import Payment
from payment.views import PaymentViewSet


class TestPaymentViewSet(APITestCase):
    # TODO
    def setUp(self):
        pass

    def test_get_all_payments(self):
        pass

    def test_fail_gat_payments(self):
        pass
