from xtypes import B_BASIC


class X_OBJ_LINE(B_BASIC):
    """
    [Type] A line
    """
    def __init__(self):
        super().__init__()
        self._k = None
        self._b = None
