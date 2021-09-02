from api.server import *

# app instance from api.server is used to feed uwsgi config


if __name__ == '__main__':
    # This section is never run when using uwsgi scripts
    run_server()
