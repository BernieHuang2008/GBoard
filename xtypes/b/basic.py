import session
from id import ID

from sympy import Interval


class B_BASIC:
    def __init__(self):
        # initial unique id
        self.id = ID()
        session.OBJECTS[self.id] = self

        # add basic attributes
        self.type = self.__class__.__name__
        self.relations = []

    def add_relation(self, relation):
        """
        Add a relation to the object
        :param relation: relation(ID)
        """
        self.relations.append(relation)

    def check_relations(self) -> bool:
        """
        Check if all the relations are satisfied
        :return: a boolean value, representing if all the relations are satisfied
        """
        for r_id in self.relations:
            rel = session.RELATIONS[r_id]
            if not rel.check():
                return False
        return True

    def movement(self) -> dict:
        pass

    def backup(self) -> dict:
        """
        Backup all the attributes of the object
        :return: a dict of all the attributes in the format of {attr_name: attr_value}
        """
        pass

    def _set(self, **kwargs):
        """
        Set the attributes of the object without checking
        """
        for k, v in kwargs.items():
            setattr(self, k, v)

    def set(self, **kwargs):
        """
        Set the attributes of the object
        :param kwargs:
        :return: True if no conflicts, False if it has conflicts
        """
        # set attributes
        self._set(**kwargs)

        # check geo-relations
        if self.check_relations():
            return True

        else:
            # backup
            backup = self.backup()

            # try to move
            m = self.movement()
            if self.set(**m):
                return True

            # restore
            self._set(**backup)
            return False

    def _equation(self):
        equs = []
        for r_id in self.relations:
            rel = session.RELATIONS[r_id]
            equs.extend(rel.equation())
        return equs
