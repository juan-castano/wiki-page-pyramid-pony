from pyramid.view import view_config

from xyz.fractals.models.wiki import Users

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Wiki Page'}
