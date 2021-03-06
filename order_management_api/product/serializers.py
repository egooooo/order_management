from rest_framework import serializers

from product.models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount']


class ProductRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'created', 'status_id', 'status', 'cashier_id',
                  'cashier', 'product_id', 'product_name',
                  'shop_assistant_id', 'shop_assistant', 'price', 'discount',
                  'final_sum']

    product_name = serializers.SerializerMethodField(source='get_product_name')
    cashier = serializers.SerializerMethodField(source='get_cashier')
    shop_assistant = serializers.SerializerMethodField(
        source='get_shop_assistant'
    )
    status = serializers.SerializerMethodField(source='get_status')
    status_id = serializers.SerializerMethodField(source='get_status_id')
    price = serializers.SerializerMethodField(source='get_price')
    discount = serializers.SerializerMethodField(source='get_discount')
    final_sum = serializers.SerializerMethodField(source='get_final_sum')

    def get_product_name(self, obj):
        if obj.product:
            return obj.product.name
        return None

    def get_cashier(self, obj):
        if obj.cashier:
            return f'{obj.cashier.first_name} {obj.cashier.last_name}'
        return None

    def get_shop_assistant(self, obj):
        if obj.shop_assistant:
            return f'{obj.shop_assistant.first_name} ' \
                   f'{obj.shop_assistant.last_name}'
        return None

    def get_status(self, obj):
        return Order.STATUS_CHOICES[obj.status][1]

    def get_status_id(self, obj):
        return obj.status

    def get_price(selfs, obj):
        return Product.objects.get(id=obj.product_id).price

    def get_discount(self, obj):
        return Product.objects.get(id=obj.product_id).discount

    def get_final_sum(self, obj):
        product = Product.objects.get(id=obj.product_id)
        return product.price - product.discount


class OrderRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'created', 'status', 'cashier_id', 'product_id',
                  'shop_assistant_id', 'price', 'discount', 'final_sum']

    price = serializers.SerializerMethodField(source='get_price')
    discount = serializers.SerializerMethodField(source='get_discount')
    final_sum = serializers.SerializerMethodField(source='get_final_sum')

    def get_price(selfs, obj):
        return Product.objects.get(id=obj.product_id).price

    def get_discount(self, obj):
        return Product.objects.get(id=obj.product_id).discount

    def get_final_sum(self, obj):
        product = Product.objects.get(id=obj.product_id)
        return product.price - product.discount
