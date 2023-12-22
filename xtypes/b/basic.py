import session
from id import ID


class B_BASIC:
    def __init__(self):
        self.id = ID()
        session.OBJECTS[self.id] = self
