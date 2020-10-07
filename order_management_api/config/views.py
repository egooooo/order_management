from django.http import JsonResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated, AllowAny

from config.settings import ENV
from config.utils import api_response


class BaseExternalView(APIView):
    permission_classes = [AllowAny]


class BaseView(APIView):
    if ENV == 'LOCAL':
        permission_classes = [AllowAny]
    else:
        permission_classes = [IsAuthenticated]


class BaseViewSet(viewsets.ModelViewSet):
    if ENV == 'LOCAL':
        permission_classes = [IsAuthenticated]
    else:
        permission_classes = [IsAuthenticated]


class BaseReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    current_user = None
    if ENV == 'LOCAL':
        permission_classes = [IsAuthenticated]
    else:
        permission_classes = [IsAuthenticated]


def error_400(request, *args, **kwargs):
    """
    Generic 400 error handler.
    """
    data = {
        'error': 'Bad request (400)'
    }
    return JsonResponse(
        api_response(data=data), status=status.HTTP_400_BAD_REQUEST
    )


def error_403(request, *args, **kwargs):
    """
    Generic 403 error handler.
    """
    data = {
        'error': 'Forbidden (403)'
    }
    return JsonResponse(
        api_response(data=data), status=status.HTTP_403_FORBIDDEN
    )


def error_404(request, *args, **kwargs):
    """
    Generic 404 error handler.
    """
    data = {
        'error': 'Page Not Found (404)'
    }
    return JsonResponse(
        api_response(data=data), status=status.HTTP_404_NOT_FOUND
    )


def error_500(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    data = {
        'error': 'Internal Server Error (500)'
    }
    return JsonResponse(
        api_response(data=data), status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
