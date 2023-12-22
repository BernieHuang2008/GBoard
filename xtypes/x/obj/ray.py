from xtypes import B_BASIC


class X_OBJ_RAY(B_BASIC):
    """
    [Type] A ray line
    """
    def __init__(self):
        super().__init__()
        self._k = None
        self._b = None
        self._origin = None
        self._direction = None
