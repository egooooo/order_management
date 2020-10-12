from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

from config.utils import api_response
from config.views import BaseReadOnlyViewSet

from payment.models import Payment
from payment.filters import PaymentFilter
from payment.serializers import PaymentSerializer

from users.models import UserProfile


class PaymentViewSet(BaseReadOnlyViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter

    def list(self, request, *args, **kwargs):
        active_user = self.request.user
        up = UserProfile.objects.get(user_id=active_user.id)

        if up.is_accountant():
            response = super(PaymentViewSet, self).list(
                request, *args, **kwargs
            )
            return Response(api_response(data=response.data))

        # 250 - Only an accountant can see transactions
        return Response(
            api_response(status_code=250),
            status=status.HTTP_400_BAD_REQUEST
        )