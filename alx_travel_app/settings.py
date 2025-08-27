INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'listings',
    'drf_yasg',
]
import environ
env = environ.Env()
environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}
