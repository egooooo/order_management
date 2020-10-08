DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = 'fvpaaq2t)(ssroa!4*mdu+3o3%x5w3ymo_0jb=b%+vpctky4h@'

ENV = 'LOCAL'
# ENV = 'DEVELOPMENT'
# ENV = 'PRODUCTION'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'om_db',
        'USER': 'om_user',
        'PASSWORD': '123qwe321',
        'HOST': 'db',
        'PORT': '5533'
    }
}
