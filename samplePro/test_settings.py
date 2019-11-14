from .settings import *

# Using in-memory database which make tests run faster
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ":memory:",
    }
}

# saving email backend to local memory to avoid sending mail to real people while testing
EMAIL_BACKEND = 'django.core.mail.backends.locem.EmailBackend'