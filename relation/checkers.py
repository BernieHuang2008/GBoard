from typing import List

import session

# TODO: remove checker
def _common_precheck(targets: List[str], types: List[str]) -> None:
    """
    [Helper] Check if the targets are formatted in the right type
    :param targets: list of targets(ID)
    :param types: list of types
    :return: None
    """
    # check type
    for i in range(len(targets)):
        p = targets[i]
        if session.OBJECTS[p].type not in types[i].split('/'):
            raise ValueError(f"Parameter `{p}` required type `{types}` instead of type `{session.OBJECTS[p].type}`")


def online(target_point: str, target_line: str) -> callable:
    """
    [Checker] Check if a point is online a line
    :param target_point: X_OBJ_POINT
    :param target_line: X_OBJ_LINE/X_OBJ_SEGMENT/X_OBJ_RAY
    :return: a checker function
    """

    def checker():
        _common_precheck(
            [target_point, target_line],
            ["X_OBJ_POINT", "X_OBJ_LINE/X_OBJ_SEGMENT/X_OBJ_RAY"]
        )

        # check if the point is on the line
        point = session.OBJECTS[target_point]
        line = session.OBJECTS[target_line]
        if point._x * line._k + line._b == point._y:
            return True
        else:
            return False

    return checker
