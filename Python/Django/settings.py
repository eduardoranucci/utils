
# 001 - Adicionar pasta templates na raiz

'''

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

'''

# 002 - Adicionar static

'''

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join('static')

'''

# 003 - Adicionar pasta de media

'''

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

'''

# 004 - Organizar os apps em uma pasta

'''

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, '../apps'))

'''

# 005 - Messages

'''

from django.contrib.messages import constants

MESSAGES_TAGS = {
    constants.DEBUG : 'alert-primary',
    constants.ERROR : 'alert-danger',
    constants.WARNING : 'alert-warning',
    constants.SUCCESS : 'alert-success',
    constants.INFO : 'alert-info',
}

--- views.py ---

from django.contrib import messages
from django.contrib.messages import constants

messages.add_message(request, constants.ERROR, 'mensagem')
return redirect('sua_view')

'''

# 006 - Trocar urls de login e logout

'''

LOGIN_URL = '/auth/login'
LOGIN_REDIRECT_URL = '/auth/home'
LOGOUT_REDIRECT_URL = '/auth/logout'

'''
