import os

# Répertoire de base du projet
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Déclaration des applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'subscriptions',
    # Ajoutez ici vos applications
]

# Middleware utilisé par Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL du site
ROOT_URLCONF = 'learn_and_films.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '/home/moukiana/learn-and-films/frontend/learn_and_films/public')],  # Chemin vers le dossier frontend
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

# Base URL pour les fichiers statiques
STATIC_URL = '/static/'

# Chemin vers les fichiers statiques
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'learn_and_films/static')]

# URL pour les fichiers media
MEDIA_URL = '/media/'

# Chemin vers les fichiers media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuration de la base de données (Exemple avec SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Autres configurations
SECRET_KEY = 'votre_cle_secrète'  # Changez ceci pour un vrai projet
DEBUG = True
ALLOWED_HOSTS = ['*']  # Ajoutez ici les hôtes autorisés pour la production

STRIPE_SECRET_KEY = 'sk_test_your_secret_key'
STRIPE_PUBLISHABLE_KEY = 'pk_test_your_publishable_key'
STRIPE_WEBHOOK_SECRET = 'whsec_your_webhook_secret'
