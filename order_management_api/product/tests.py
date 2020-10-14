from rest_framework.test import APIRequestFactory, APITestCase, \
    force_authenticate

from django.contrib.auth.models import User
from product.models import Product, Order
from product.views import ProductViewSet, OrderViewSet


class TestProductViewSet(APITestCase):
    fixtures = ['roles', 'auth_user.json', 'user.json', 'products.json']

    def setUp(self):
        # create test request (.get(), post(), .put(), .delete())
        self.factory = APIRequestFactory()
        self.user = User.objects.get(id=1)

    def test_get_all_products(self):
        # TODO
        expected_products_data = [
            {
                "id": 1,
                "name": "TV",
                "price": 3000000,
                "discount": 0,
            },
            {
                "id": 2,
                "name": "Mobile phone",
                "price": 2500000,
                "discount": 0,
            },
            {
                "id": 3,
                "name": "iMac",
                "price": 12000000,
                "discount": 0,
            },
            {
                "id": 4,
                "name": "MacBook PRO",
                "price": 9200000,
                "discount": 0,
            }
        ]


        view = ProductViewSet.as_view({"get": "list"})
        url = 'product/'
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request)

        products_data = response.data.get('result').get('results')
        #products_data = list()

        for product in expected_products_data:
            self.assertIn(product, products_data)

    def test_get_product(self):
        view = ProductViewSet.as_view({"get": "retrieve"})
        url = 'product/<int:product_id>//'
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request, product_id=1)

        product_data = response.data.get('result')
        # product_data = dict()
        self.assertDictEqual(
            {
                'id': 1,
                'name': 'TV',
                'price': 3000000,
                'discount': 0
            },
            product_data
        )

    def test_fail_get_product(self):
        expected_error = {
            'error': {
                'code': 220,
                'message': 'Товар не знайдено'
            },
            'result': None
        }
        view = ProductViewSet.as_view({"get": "retrieve"})
        url = 'product/<int:product_id>/'
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request, product_id=5)
        response_data = response.data
        self.assertDictEqual(expected_error, response_data)

    def test_created_product(self):
        product_data = {
            "name": "iPod",
            "price": 2300000
        }
        view = ProductViewSet.as_view({"post": "post"})
        url = 'product/'
        request = self.factory.post(url, product_data)
        force_authenticate(request, user=self.user)
        response = view(request)
        response_data = response.data.get('result')
        self.assertEqual(5, response_data)

    def test_fail_created_product(self):
        product_data = {
            "name": "",
            "price": 2300000
        }
        view = ProductViewSet.as_view({"post": "post"})
        url = 'product/'
        request = self.factory.post(url, product_data)
        force_authenticate(request, user=self.user)
        response = view(request)
        response_data = response.data
        response_error = response_data.get('error')
        self.assertDictEqual(
            {
                'code': 100,
                'message': 'Не передані всі необхідні дані'
            },
            response_error
        )

    def test_update_product(self):
        product_data = {
            "name": "iPod Nano"
        }
        view = ProductViewSet.as_view({"put": "put"})
        url = 'product/<int:product_id>/'
        request = self.factory.put(url, product_data)
        force_authenticate(request, user=self.user)
        response = view(request, product_id=1)
        response_data = response.data.get('result')

        product = Product.objects.get(name="iPod Nano")

        self.assertEqual(True, response_data)
        self.assertEqual(product_data.get('name'), product.name)

    def test_fail_update_product(self):
        expected_error = {
            'code': 220,
            'message': 'Товар не знайдено'
        }
        view = ProductViewSet.as_view({"put": "put"})
        url = 'product/<int:product_id>/'
        request = self.factory.put(url)
        force_authenticate(request, user=self.user)
        response = view(request, product_id=5)
        response_data = response.data
        self.assertDictEqual(expected_error, response_data.get('error'))

    def test_delete_product(self):
        view = ProductViewSet.as_view({"delete": "delete"})
        url = 'product/<int:product_id>//'
        request = self.factory.delete(url)
        force_authenticate(request, user=self.user)
        response = view(request, product_id=1)
        product_data = response.data.get('result')
        self.assertEqual(True, product_data)

    def test_fail_delete_prosuct(self):
        expected_error = {
            'code': 220,
            'message': 'Товар не знайдено'
        }
        view = ProductViewSet.as_view({"delete": "delete"})
        url = 'product/<int:product_id>/'
        request = self.factory.delete(url)
        force_authenticate(request, user=self.user)
        response = view(request, product_id=5)
        response_data = response.data
        self.assertDictEqual(expected_error, response_data.get('error'))
