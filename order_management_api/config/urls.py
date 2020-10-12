"""
    URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls', namespace='auth')),
    path('users/', include('users.urls', namespace='user')),
    path('product/', include('product.urls', namespace='product')),
    path('payment/', include('payment.urls', namespace='payment')),
]

handler400 = 'config.views.error_400'
handler403 = 'config.views.error_403'
handler404 = 'config.views.error_404'
handler500 = 'config.views.error_500'
