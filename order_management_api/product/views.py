from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

from config.utils import api_response
from config.views import BaseReadOnlyViewSet

from product.models import Product, Order
from product.filters import ProductFilter, OrderFilter
from product.serializers import ProductSerializer, ProductRetrieveSerializer, \
    OrderSerializer, OrderRetrieveSerializer

from users.models import UserProfile

import datetime


class ProductViewSet(BaseReadOnlyViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def list(self, request, *args, **kwargs):
        response = super(ProductViewSet, self).list(
            request, *args, **kwargs
        )
        return Response(api_response(data=response.data))

    def post(self, request):
        data = request.data

        try:
            product = Product()
            product.name = data.get('name')
            product.price = data.get('price')
            product.save()
            return Response(api_response(data=product.id))

        except Exception as e:
            # 999 - Unhandled exception
            return Response(
                api_response(status_code=999, message=str(e)),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def retrieve(self, request, product_id=None, *args, **kwargs):
        try:
            product = Product.objects.get(id=self.kwargs.get('product_id'))
        except:
            # 220 - Product not found
            return Response(
                api_response(status_code=220),
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProductRetrieveSerializer(product)
        return Response(api_response(data=serializer.data))

    def put(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except:
            # 220 - Product not found
            return Response(
                api_response(status_code=220),
                status=status.HTTP_400_BAD_REQUEST
            )

        if request.data.get('name'):
            product.name = request.data.get('name')
        if request.data.get('price'):
            product.price = request.data.get('price')
        product.save()

        return Response(api_response(data=True))

    def delete(self, request, product_id):
        try:
            Product.objects.get(id=product_id).delete()
            return Response(api_response(data=True))
        except:
            # 220 - Product not found
            return Response(
                api_response(status_code=220),
                status=status.HTTP_400_BAD_REQUEST
            )


class OrderViewSet(BaseReadOnlyViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

    def get_queryset(self):
        active_user = self.request.user
        up = UserProfile.objects.get(user_id=active_user.id)

        if up.is_cashier():
            return self.queryset.filter(status=1)

        if up.is_shop_assistant():
            return self.queryset.filter(status=0)

        return self.queryset

    def list(self, request, *args, **kwargs):
        response = super(OrderViewSet, self).list(
            request, *args, **kwargs
        )
        return Response(api_response(data=response.data))

    def post(self, request):
        data = request.data

        active_user = self.request.user
        up = UserProfile.objects.get(user_id=active_user.id)

        if up.is_cashier() is not True:
            # 221 - Only the cashier can create an order.
            return Response(
                api_response(status_code=221),
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = Product.objects.get(id=data.get('product_id'))
        except:
            # 220 - Product not found
            return Response(
                api_response(status_code=220),
                status=status.HTTP_400_BAD_REQUEST
            )

        # for discount
        today = datetime.date.today()
        day = today.day
        month = (today.month - 1) % 12
        year = today.year + ((today.month - 1) // 12)
        one_month_ago = datetime.date(year, month, day)

        product_created = product.created.strftime("%Y-%m-%d")
        one_month_ago = one_month_ago.strftime("%Y-%m-%d")

        if one_month_ago >= product_created:
            product.discount = (product.price * 20) / 100
            product.save()

        # create new order
        order = Order()
        order.status = 0
        order.cashier_id = up.id
        order.product_id = product.id
        order.save()

        return Response(api_response(data=order.id))

    def retrieve(self, request, order_id=None, *args, **kwargs):
        try:
            order = Order.objects.get(id=self.kwargs.get('order_id'))
        except:
            # 222 - Order not found
            return Response(
                api_response(status_code=222),
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = OrderRetrieveSerializer(order)
        return Response(api_response(data=serializer.data))

    def put(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except:
            # 222 - Order not found
            return Response(
                api_response(status_code=222),
                status=status.HTTP_400_BAD_REQUEST
            )

        active_user = self.request.user
        up = UserProfile.objects.get(user_id=active_user.id)

        order.status = request.data.get('status')
        order.shop_assistant_id = up.id
        order.save()

        return Response(api_response(data=True))
