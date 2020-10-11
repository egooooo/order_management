from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('', views.UserProfileViewSet.as_view({
        'get': 'list'
    }), name='users'),
    path('<int:user_id>/', views.UserProfileViewSet.as_view({
        'get': 'retrieve',
    }), name='user'),
    path('roles/', views.UserRoleViewSet.as_view({
        'get': 'list'
    }), name='roles'),
]
