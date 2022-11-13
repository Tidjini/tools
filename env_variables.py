"""Get Environment Variables for Local Configurations

Like Django Secret Key, store the value in your machine, and call it with Python os module.

IMPORTANT: For best practice, avoid to import Django modules in settings files.
django made an exception just for ImproperlyConfigured  
"""

import os
from django.core.exceptions import ImproperlyConfigured


def get_environment_variable(var_name: str, default: str = None) -> str:
    """Get environment variable with os module

    set default for default value
    """
    try:
        return os.environ.get(var_name, default) if default else os.environ[var_name]
    except ImproperlyConfigured:
        message = "Set {} the environment variable, in your local machine".format(
            var_name
        )
        raise ImproperlyConfigured(message)
