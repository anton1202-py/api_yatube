from django.core.wsgi import get_wsgi_application

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatube_api.settings')

application = get_wsgi_application()
