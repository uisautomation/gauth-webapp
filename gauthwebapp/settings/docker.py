import os

# Import settings from the base settings file
from .base import *  # noqa: F401, F403

# Ensure that DEBUG is not set
DEBUG = False

# All hosts are allowed to connect to the container by default
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')
