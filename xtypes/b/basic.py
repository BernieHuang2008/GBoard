import session
from id import ID


class B_BASIC:
    def __init__(self):
        # initial unique id
        self.id = ID()
        while self.id in session.OBJECTS:
            self.id = ID()
        session.OBJECTS[self.id] = self

        # add basic attributes
        self.type = self.__class__.__name__
        self.relations = []

    def add_relation(self, relation):
        self.relations.append(relation)
