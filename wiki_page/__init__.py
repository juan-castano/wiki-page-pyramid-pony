from pyramid.config import Configurator

from pony.orm import Database

# Define manager database
database = Database()

def __initialize_database():
    """Generate new database instance single reference for managing database"""
    print("Generating database")
    try:
        database.bind(provider='sqlite', filename='wiki_page.sqlite', create_db=True)
        database.generate_mapping(create_tables=True)
    except Exception as ex:
        print("Unexpected error: {}".format(ex))
    

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    __initialize_database()
    return config.make_wsgi_app()
