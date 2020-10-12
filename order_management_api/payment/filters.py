import django_filters

from django_filters import rest_framework as filters

from payment.models import Payment


class PaymentFilter(filters.FilterSet):
    class Meta:
        model = Payment
        fields = ['id', 'created', 'amount', 'status']
        order_by = model()._meta.ordering

    order = filters.OrderingFilter(
        fields=['id', 'created', 'status']
    )
    # Dates filter (created_before, created_after)
    created = django_filters.DateFromToRangeFilter()
    # amount_from, amount_to
    amount = django_filters.RangeFilter()
