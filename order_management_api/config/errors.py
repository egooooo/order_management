
api_errors = [
    {
        'code': 100,
        'message': {
            'ru': 'Не переданы все необходимые данные',
            'en': 'Wrong input data',
            'uk': 'Не передані всі необхідні дані'
        }
    },
    {
        'code': 101,
        'message': {
            'ru': 'Ошибка выполнения SQL запроса',
            'en': 'SQL request error',
            'uk': 'Помилка виконання SQL запиту'
        }
    },
    {
        'code': 102,
        'message': {
            'ru': 'Не верный формат запроса',
            'en': 'Wrong request',
            'uk': 'Не вірний формат запиту'
        }
    },
    {
        'code': 103,
        'message': {
            'ru': 'Неуспешная авторизация',
            'en': 'Authentication error',
            'uk': 'Неуспішна авторизація'
        }
    },
    {
        'code': 104,
        'message': {
            'ru': 'Не передан авторизационный токен',
            'en': 'Authorization token missing',
            'uk': 'Не переданий авторизаційний токен'
        }
    },
    {
        'code': 105,
        'message': {
            'ru': 'Некорректный авторизационный токен',
            'en': 'Invalid authorization token',
            'uk': 'Некоректний авторизаційний токен'
        }
    },
    {
        'code': 106,
        'message': {
            'ru': 'Время действия токена истекло',
            'en': 'Authorization token expired',
            'uk': 'Час дії токена минув'
        }
    },
    {
        'code': 107,
        'message': {
            'ru': 'Некорректный результат SQL запроса',
            'en': 'Incorrect DB response data',
            'uk': 'Некоректний результат SQL запиту'
        }
    },
    {
        'code': 108,
        'message': {
            'ru': 'Неверный пароль',
            'en': 'Incorrect password',
            'uk': 'Невірний пароль'
        }
    },
    {
        'code': 109,
        'message': {
            'ru': 'Ошибка формирования токена',
            'en': 'JWT building error',
            'uk': 'Помилка формування токена'
        }
    },
    {
        'code': 110,
        'message': {
            'ru': 'Пользователь не найден или не активен',
            'en': 'User not found or inactive',
            'uk': 'Користувач не знайдений або не активний'
        }
    },
    {
        'code': 111,
        'message': {
            'ru': 'Ошибка 2FA авторизации. Ключ неверный',
            'en': '2FA failed! OTP key wrong',
            'uk': 'Помилка 2FA авторизації. Ключ невірний'
        }
    },
    {
        'code': 112,
        'message': {
            'ru': 'Неверно указан интервал периода дат',
            'en': 'Invalid date period interval',
            'uk': 'Невірно вказано інтервал періоду дат'
        }
    },
    {
        'code': 113,
        'message': {
            'ru': 'Пароль не совпадает',
            'en': 'Password does not match',
            'uk': 'Пароль не збігається'
        }
    },

    # User 150-199
    {
        'code': 150,
        'message': {
            'ru': 'Пользователь не найден',
            'en': 'User not found',
            'uk': 'Користувач не знайдений'
        }
    },
    {
        'code': 151,
        'message': {
            'ru': 'Только администратор может создавать пользователей',
            'en': 'Only admin can create users',
            'uk': 'Тільки адміністратор може створювати користувачів'
        }
    },

    # Role 200-219
    {
        'code': 200,
        'message': {
            'ru': 'Роль не найдена',
            'en': 'Role not found',
            'uk': 'Посада не знайдена'
        }
    },
    {
        'code': 201,
        'message': {
            'ru': 'Доступно только для роли администратор',
            'en': 'Only available for the administrator role',
            'uk': 'Доступно тільки для ролі адміністратор'
        }
    },

    # Product, Order 220-249
    {
        'code': 220,
        'message': {
            'ru': 'Товар не найден',
            'en': 'Product not found',
            'uk': 'Товар не знайдено'
        }
    },
    {
        'code': 221,
        'message': {
            'ru': 'Только кассир может создать заказ.',
            'en': 'Only the cashier can create an order.',
            'uk': 'Тільки касир може створити замовлення.'
        }
    },
    {
        'code': 222,
        'message': {
            'ru': 'Закащ не найден',
            'en': 'Order not found',
            'uk': 'Замовлення не знайдено'
        }
    },
    {
        'code': 223,
        'message': {
            'ru': 'Только продавец-консультант может обновить заказ.',
            'en': 'Only the shop assistant can update an order.',
            'uk': 'Тільки продавець-консультант може оновити замовлення.'
        }
    },

    # System error
    {
        'code': 999,
        'message': {
            'ru': 'Системная ошибка',
            'en': 'System internal error',
            'uk': 'Системна помилка'
        }
    },
]


def get_error(code):
    for error in api_errors:
        if error['code'] == code:
            return error
    return False
