from typing import List
from sympy import Eq

import session


def online(target_point: str, target_line: str) -> List[Eq]:
    """
    [Checker] Check if a point is online a line
    :param target_point: X_OBJ_POINT
    :param target_line: X_OBJ_LINE/X_OBJ_SEGMENT/X_OBJ_RAY
    :return: a sympy equation
    """
    # check type
    if session.OBJECTS[target_point].type != 'X_OBJ_POINT':
        raise ValueError(f"Parameter `{target_point}` required type `X_OBJ_POINT` instead of type `{session.OBJECTS[target_point].type}`")
    if session.OBJECTS[target_line].type not in ['X_OBJ_LINE', 'X_OBJ_SEGMENT', 'X_OBJ_RAY']:
        raise ValueError(f"Parameter `{target_line}` required type `X_OBJ_LINE/X_OBJ_SEGMENT/X_OBJ_RAY` instead of type `{session.OBJECTS[target_line].type}`")

    # check if the point is on the line
    point = session.OBJECTS[target_point]
    line = session.OBJECTS[target_line]
    return [Eq(point._x * line._k + line._b, point._y)]

