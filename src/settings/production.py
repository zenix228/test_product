from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'URL': 'postgres://zzvyldlf:av5LtXO5sGaLvBTQr9iVhD-ka_IlDQdE@floppy.db.elephantsql.com/zzvyldlf',
        'NAME': 'zzvyldlf',
        'USER': 'zzvyldlf',
        'PASSWORD': 'av5LtXO5sGaLvBTQr9iVhD-ka_IlDQdE',
        'HOST': 'floppy.db.elephantsql.com',
    }
}