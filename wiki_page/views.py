from pyramid.view import view_config

from pony import orm

from .xyz.wiki import User

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
@orm.db_session
def my_view(request):
    return {'project': 'Wiki Page'}


@view_config(route_name='user', renderer='json')
@orm.db_session
def user_view(request):
    user = User(name="Juan")
    print(user.to_json())
    return {'project': user.to_json()}