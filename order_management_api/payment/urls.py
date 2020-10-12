from django.urls import path

from . import views


app_name = 'payment'

urlpatterns = [
    path('', views.PaymentViewSet.as_view({
        'get': 'list'
    }), name='payments')
]
