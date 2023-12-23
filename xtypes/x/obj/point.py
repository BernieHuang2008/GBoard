import sympy

from xtypes import B_BASIC


class X_OBJ_POINT(B_BASIC):
    """
    [Type] A point
    """

    def __init__(self):
        super().__init__()
        self._x = None
        self._y = None

    def movement(self) -> dict:
        # backup
        backup = self.backup()

        # set unknowns
        self._x = sympy.Symbol('_x')
        self._y = sympy.Symbol('_y')

        # solve equation
        equation = self._equation()
        solution = sympy.solve(equation, self._x, self._y)

        if not solution:
            # restore
            self._set(backup)
            return None
        if isinstance(solution, list):  # multiple solution
            solution = solution[0]

        return {
            '_x': solution[self._x],
            '_y': solution[self._y],
        }
