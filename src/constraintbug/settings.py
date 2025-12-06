INSTALLED_APPS = [
    'constraintbug',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'constraintbug',
        'USER': 'constraintbug',
        'PASSWORD': 'constraintbug',
        'HOST': 'db',
        'PORT': '5432',
    }
}
