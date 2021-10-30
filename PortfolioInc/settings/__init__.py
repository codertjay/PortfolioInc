from decouple import config

if config('DEBUG') == 'True':
    from .local import *
else:
    from .production import *

