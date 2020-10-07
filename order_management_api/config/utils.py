import datetime
import logging
import traceback

from django.utils import timezone

from config.base import LANGUAGE_CODE
from .errors import get_error


logger = logging.getLogger(__name__)


def api_response(data=None, status_code=0, lang=None, message=None):
    """
        Method standardizes API response
    """
    response = {
        'error': {
            'code': status_code,
            'message': ''
        },
        'result': data
    }

    if not lang:
        lang = LANGUAGE_CODE

    if status_code and get_error(status_code):
        response['error']['message'] = get_error(status_code)['message'][lang]

        logger.error(f"{response}")
        logger.error(f"{traceback.format_exc()}")

    if message:
        logger.error(f"{response['error']['message']} ({message})")
        logger.error(f"{traceback.format_exc()}")

        response['error']['message'] += " (" + message + ")"

    return response


def parse_datetime(dt, format):
    current_tz = timezone.utc
    ded = datetime.datetime.strptime(dt, format)
    return current_tz.localize(ded)
