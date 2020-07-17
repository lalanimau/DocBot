# -*- coding: utf-8 -*-

import os

DEBUG = False

PLUGINS = [
    'docbot.plugins',
]

ERRORS_TO = None

TIMEOUT = 100

API_TOKEN = ''  #Enter your api token here 

ALIASES = ''

DEFAULT_REPLY = "Sorry but I couldn't get you"

for key in os.environ:
    if key[:9] == 'docbot_':
        name = key[9:]
        globals()[name] = os.environ[key]

try:
    from docbot_settings import *
except ImportError:
    try:
        from local_settings import *
    except ImportError:
        pass

# convert default_reply to DEFAULT_REPLY
try:
    DEFAULT_REPLY = default_reply
except NameError:
    pass
