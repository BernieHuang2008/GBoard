from xtypes import B_BASIC


class X_OBJ_SEGMENT(B_BASIC):
    """
    [Type] A segment
    """
    def __init__(self):
        super().__init__()
        self._k = None
        self._b = None
        self._start = None
        self._end = None
