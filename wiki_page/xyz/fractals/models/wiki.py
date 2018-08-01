from wiki_page import database

from pony import orm


class User(database.Entity):
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str)