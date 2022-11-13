"""BASE_DIR using pathlib

use this in your django. 
settings/base.py
"""

from pathlib import Path

# settings/base.py .. settings .. project
BASE_DIR = Path(__file__).resolve().parent


MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "static_root"

# for django staticfiles directory
STATICFILES_DIR = [BASE_DIR / "static"]

# example of using BASE_DIR, in templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
    }
]
