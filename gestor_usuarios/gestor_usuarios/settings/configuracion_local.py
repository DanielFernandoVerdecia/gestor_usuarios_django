from .configuracion_base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("DB_NAME"),
        'USER': get_secret("USER"),
        'PASSWORD' : get_secret("PASSWORD"),
        'HOST' :  'localhost',
        'PORT' : '5432' 
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#esto es para los estilos css u otros archivos o imagenes
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

#esto hace parte para generar la URL de una imagen
MEDIA_URL = '/show_img/'
MEDIA_ROOT = BASE_DIR.child('imgs')