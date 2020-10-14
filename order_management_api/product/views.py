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
from payment.models import Payment

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

        if data.get('name') == "":
            # 100 - Wrong input data
            return Response(
                api_response(status_code=100),
                status=status.HTTP_400_BAD_REQUEST
            )

        product = Product()
        product.name = data.get('name')
        product.price = data.get('price')
        product.save()
        return Response(api_response(data=product.id))

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

        # TODO need method
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

        if up.is_cashier():
            change = 0
            product = Product.objects.get(id=order.product_id)
            product_price = product.price - product.discount

            if 'amount' in request.GET:
                if int(request.GET['amount']) < product_price:
                    # 225 - Amount to be paid is less than the
                    # sum of the product
                    return Response(
                        api_response(status_code=225),
                        status=status.HTTP_400_BAD_REQUEST
                    )

            if 'amount' in request.GET:
                if int(request.GET['amount']) >= product_price:
                    change = int(request.GET['amount']) - product_price

            pay = Payment()
            # TODO invoice_date_created save to db
            pay.order_id = order.id
            if request.GET['is_cash'] == 'true':
                pay.cash = True
                pay.amount = request.GET['amount']
                pay.change = change
            if request.GET['is_cash'] == 'false':
                pay.card = True
                pay.amount = product_price
                pay.change = change
            pay.status = 1
            pay.save()

            result = dict()
            result['product_name'] = product.name
            result['cashier_name'] = f'{up.first_name} {up.last_name}'
            result['order_created_date'] = order.created
            result['invoice_date_created'] = pay.invoice_date_created
            result['product_price'] = product.price
            result['product_discount'] = product.discount
            result['to_pay_amount'] = pay.amount
            if pay.cash is True:
                result['pay_cash'] = True
            if pay.card is True:
                result['pay_card'] = True
            result['pay_change'] = pay.change

            order.status = 2
            order.save()

            return Response(api_response(data=result))


        if up.is_shop_assistant():
            if 'shop_assistant_check_product' in request.GET:
                if request.GET['shop_assistant_check_product'] == 'true':
                    order.status = 1
                    order.shop_assistant_id = up.id
                    order.save()
                    return Response(api_response(data=True))

        order.status = 3
        order.save()
        # 224 - The order was not verified. Status - canceled.
        return Response(
            api_response(status_code=224),
            status=status.HTTP_400_BAD_REQUEST
        )
