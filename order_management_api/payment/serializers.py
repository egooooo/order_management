from rest_framework import serializers

from payment.models import Payment
from product.models import Order


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'created', 'order_id', 'status_id', 'status',
                  'cashier_id', 'cashier', 'product_id', 'product_name',
                  'shop_assistant_id', 'shop_assistant', 'product_price',
                  'product_discount', 'cash', 'card', 'amount', 'change']

    product_id = serializers.SerializerMethodField(source='get_product_id')
    product_name = serializers.SerializerMethodField(source='get_product_name')
    cashier_id = serializers.SerializerMethodField(source='get_cashier_id')
    cashier = serializers.SerializerMethodField(source='get_cashier')
    status = serializers.SerializerMethodField(source='get_status')
    status_id = serializers.SerializerMethodField(source='get_status_id')
    shop_assistant = serializers.SerializerMethodField(
        source='get_shop_assistant'
    )
    shop_assistant_id = serializers.SerializerMethodField(
        source='get_shop_assistant_id'
    )
    product_price = serializers.SerializerMethodField(
        source='get_product_price'
    )
    product_discount = serializers.SerializerMethodField(
        source='get_product_discount'
    )

    def get_product_id(self, obj):
        if obj.order:
            if obj.order.product:
                return obj.order.product.id
        return None

    def get_product_name(self, obj):
        if obj.order:
            if obj.order.product:
                return obj.order.product.name
        return None

    def get_cashier_id(self, obj):
        if obj.order:
            if obj.order.cashier:
                return obj.order.cashier.id
        return None

    def get_cashier(self, obj):
        if obj.order:
            if obj.order.cashier:
                return f'{obj.order.cashier.first_name} ' \
                       f'{obj.order.cashier.last_name}'
        return None

    def get_shop_assistant_id(self, obj):
        if obj.order:
            if obj.order.shop_assistant:
                return obj.order.shop_assistant.id
        return None

    def get_shop_assistant(self, obj):
        if obj.order:
            if obj.order.shop_assistant:
                return f'{obj.order.shop_assistant.first_name} ' \
                       f'{obj.order.shop_assistant.last_name}'
        return None

    def get_status(self, obj):
        if obj.status:
            return Order.STATUS_CHOICES[obj.status][1]
        return None

    def get_status_id(self, obj):
        return obj.status

    def get_product_price(selfs, obj):
        if obj.order:
            if obj.order.product:
                return obj.order.product.price
        return None

    def get_product_discount(self, obj):
        if obj.order:
            if obj.order.product:
                return obj.order.product.discount
        return None
