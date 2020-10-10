DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = 'fvpaaq2t)(ssroa!4*mdu+3o3%x5w3ymo_0jb=b%+vpctky4h@'

ENV = 'LOCAL'
# ENV = 'DEVELOPMENT'
# ENV = 'PRODUCTION'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'order_db',
        'USER': 'order_user',
        'PASSWORD': '123qwe321',
        'HOST': 'postgresql',
        'PORT': '5454'
    }
}
