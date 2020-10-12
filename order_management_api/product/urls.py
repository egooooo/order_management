from django.urls import path

from . import views


app_name = 'product'

urlpatterns = [
    path('', views.ProductViewSet.as_view({
        'get': 'list',
        'post': 'post'
    }), name='products'),
    path('<int:product_id>/', views.ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'put'
    }), name='product'),
    path('<int:product_id>/delete/', views.ProductViewSet.as_view({
        'delete': 'delete'
    }), name='product_delete'),
    path('order/', views.OrderViewSet.as_view({
        'get': 'list',
        'post': 'post'
    }), name='order_products'),
    path('order/<int:order_id>/', views.OrderViewSet.as_view({
        'get': 'retrieve',
        'put': 'put'
    }), name='order_product'),
]
