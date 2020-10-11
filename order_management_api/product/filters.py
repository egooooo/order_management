import django_filters

from django_filters import rest_framework as filters
from django.db.models import Q

from product.models import Product, Order


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount']
        order_by = model()._meta.ordering

    order = filters.OrderingFilter(
        fields=['id', 'name', 'price', 'discount']
    )


class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = ['id', 'created', 'status', 'cashier_id', 'product_id',
                  'shop_assistant_id']
        order_by = model()._meta.ordering

    order = filters.OrderingFilter(
        fields=['id', 'created', 'status', 'cashier_id', 'product_id',
                'shop_assistant_id']
    )
    # Dates filter (created_before, created_after)
    created = django_filters.DateTimeFromToRangeFilter()
