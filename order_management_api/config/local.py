DEBUG = True
ALLOWED_HOSTS = ['*']

# For local use only
SECRET_KEY = 'fvpaaq2t)(ssroa!4*mdu+3o3%x5w3ymo_0jb=b%+vpctky4h@'

ENV = 'LOCAL'
# ENV = 'DEVELOPMENT'
# ENV = 'PRODUCTION'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'order_management_db',
        'USER': 'order_management_user',
        'PASSWORD': '123qwe321',
        'HOST': 'postgresql',
        'PORT': '5454'
    }
}

# FIXTURES

FIXTURE_DIRS = (
   'order_management_api/fixture/',
)