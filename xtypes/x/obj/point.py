from xtypes import B_BASIC


class X_OBJ_POINT(B_BASIC):
    """
    [Type] A point
    """
    def __init__(self):
        super().__init__()
        self._x = None
        self._y = None
