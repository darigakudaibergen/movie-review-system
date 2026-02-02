"""
ASGI config for movie_review project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_review.settings')

application = get_asgi_application()
