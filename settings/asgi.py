import os
import sys
from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PATHS = [os.path.realpath(os.path.join(BASE_DIR, 'apps'))]
for path in PATHS:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings_development')

application = get_wsgi_application()
