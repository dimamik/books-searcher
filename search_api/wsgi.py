import sys

import config
# app instance from api.server is used to feed uwsgi config
from api.server import *

# WARNING! config import initializes config


if __name__ == '__main__':
    # This section is never run when using uwsgi scripts
    config.parse_args(sys.argv)
    run_server()
