from pyramid.config import Configurator
import sqlite3

def db_connect(request):
    def db_close(request):
        if con is not None:
            con.close()
    con = sqlite3.connect(request.registry.settings['sqlite_connection_string'])
    request.add_finished_callback(db_close)
    return con

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.add_request_method(db_connect, 'db')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
