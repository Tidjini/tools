'''Get Secret Information by json file

For example Django Secret Key (or other infromation), store values json file.

IMPORTANT: For best practice, avoid to import Django modules in settings files.
django made an exception just for ImproperlyConfigured  
'''

import json
from django.core.exceptions import ImproperlyConfigured

with open('secrets.json') as config:
    secrets = json.load(config)


def get_secret_information(key_information: str, secrets: Any = secrets, default: str = None) -> str:
    '''Get Secrets Information from a Json File'''
    try:
        return secrets.get(key_information, default) if default else secrets[key_information]

    except ImproperlyConfigured:
        message = "Set {}, in your {} config file..".format(
            key_information, secrets)
        raise ImproperlyConfigured(message)
