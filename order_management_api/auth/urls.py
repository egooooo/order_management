from django.urls import path

from . import views

app_name = 'auth'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='nbu_today'),
    path('registration/', views.RegistrationView.as_view(), name='user'),
]
