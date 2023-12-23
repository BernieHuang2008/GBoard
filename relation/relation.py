from typing import Dict, Any, List
from sympy import Eq

import session
from . import checkers
from . import equa
from id import ID


class GeoRelation:
    def __init__(self, name=None, description=None, type=None, objects=None, checker=None, equation=None):
        self.id = ID()
        session.RELATIONS[self.id] = self
        self.name = name
        self.desc = description
        self.type = type
        self.objects = objects
        self.check = checker(*self.objects)
        self._equation = equation

        self._params = {}

    presets = {
        'online': {
            'name': 'online',
            'description': 'on a line',
            'type': 'online',
            'objects': ['X_OBJ_POINT: target_point', 'X_OBJ_LINE/X_OBJ_SEGMENT/X_OBJ_RAY: target_line'],
            'checker': checkers.online,
            'equation': equa.online,
        },
        'xypoint': {
            'name': 'point',
            'description': 'locate a point with its x-y-coordinates',
            'type': 'xypoint',
            'objects': ['T_INT: x_coord', 'T_INT: y_coord'],
            'checker': None,
            'equation': None,
        },
    }

    @staticmethod
    def _sort_param_list(params: Dict[str, Any], target_format: List[str]) -> list:
        """
        Sort the param list
        :param params: a dict of {para_name: obj_id/immediate_value}
        :param target_format: the list of target format
        :return: a list of objects in the right order
        """
        # format the objects list
        formatted_objs = []
        for obj_definition in target_format:
            obj_type, obj_name = obj_definition.split(':')
            obj_name = obj_name.strip()
            target = params[obj_name]
            # check type
            if obj_type.startswith('X_OBJ_'):
                if session.OBJECTS[target].type in obj_type.split('/'):
                    formatted_objs.append(target)
                else:
                    raise ValueError(
                        f"Object `{obj_name}` required type `{obj_type}` instead of type `{session.OBJECTS[target].type}`")
            else:
                formatted_objs.append(target)

        return formatted_objs

    @classmethod
    def from_preset(cls, rel_name: str, rel_params: Dict[str, Any]):
        """
        Create a relation from the preset list
        :param rel_name: relation name
        :param rel_params: relation parameters, a dict of {para_name: obj_id/immediate_value}
        :return: a relation
        """
        # get the preset
        preset = cls.presets[rel_name]

        # sort the objects list
        formatted_objs = cls._sort_param_list(rel_params, preset['objects'])

        # create the relation
        return cls(name=preset['name'],
                   description=preset['description'],
                   type=preset['type'],
                   objects=formatted_objs,
                   checker=preset['checker'],
                   equation=preset['equation'],
                   )

    @classmethod
    def relate(cls, rel_name: str, rel_params: Dict[str, Any]):
        """
        Create a relation from the preset list, and bind it to the involved objects
        :param rel_name: relation name
        :param rel_params: relation parameters, a dictionary of {para_name: obj_id/immediate_value}
        :return: a relation
        """
        # sort the objects list
        preset = cls.presets[rel_name]
        formatted_objs = cls._sort_param_list(rel_params, preset['objects'])

        # create a new relation
        rel = cls.from_preset(rel_name, rel_params)
        rel._params = {preset['objects'][i]: formatted_objs[i] for i in range(len(formatted_objs))}

        # bind the relation to the objects
        for i in range(len(formatted_objs)):
            # get the target
            target_id = formatted_objs[i]
            target = session.OBJECTS[target_id]
            # add the relation
            target.add_relation(rel.id)

    def equation(self) -> List[Eq]:
        """
        Get the equation of the relation
        :return: a list of sympy equations
        """
        return self._equation(*self.objects)
