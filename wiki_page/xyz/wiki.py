from wiki_page import database

from pony import orm

import json

class User(database.Entity):
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str)

    def __ini__(self, name=None):
        self.name = name

    def to_json(self):
        return json.dumps(self.__dict__)
