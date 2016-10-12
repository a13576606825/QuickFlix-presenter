"""
App
~~~

The Flask's `app` instance is initialized in this module.

Currently, the configuration is simple. We don't need to set any custom configuration
to Flask.
"""

import logging
from flask import Flask

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

app = Flask(__name__)
log.info('Presenter is initialized.')
