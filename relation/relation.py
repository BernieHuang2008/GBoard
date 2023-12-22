import session
from . import checkers
from id import ID


class GeoRelation:
    def __init__(self, name=None, description=None, type=None, objects=None, checker=None):
        self.id = ID()
        self.name = name
        self.desc = description
        self.type = type
        self.objects = objects
        self.check = checker

    presets = {
        'online': {
            'name': 'online',
            'description': 'on a line',
            'type': 'online',
            'objects': ['X_OBJ_POINT: target_point', 'X_OBJ_LINE/X_OBJ_SEGMENT/X_OBJ_RAY: target_line'],
            'checker': checkers.online
        },
        'xypoint': {
            'name': 'point',
            'description': 'fixed on a point',
            'type': 'xypoint',
            'objects': ['T_INT: x_coord', 'T_INT: y_coord']
        },
    }

    @classmethod
    def from_preset(cls, name: str, objs: dict, isMajor: bool):
        # get the preset
        preset = cls.presets[name]

        # format the objects list
        formatted_objs = []
        for obj_definition in preset['objects']:
            obj_type, obj_name = obj_definition.split(':')
            obj_name = obj_name.strip()
            target = objs[obj_name]
            # check type
            if obj_type.startswith('X_OBJ_'):
                if session.OBJECTS[target].type in obj_type.split('/'):
                    formatted_objs.append(target)
                else:
                    raise ValueError(
                        f"Object `{obj_name}` required type `{obj_type}` instead of type `{session.OBJECTS[target].type}`")
            else:
                formatted_objs.append(target)

        # create the relation
        return cls(name=preset['name'],
                   description=preset['description'],
                   type=('' if isMajor else '.') + preset['type']
                   )
