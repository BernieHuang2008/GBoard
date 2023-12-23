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

    def backup(self) -> dict:
        return {
            '_x': self._x,
            '_y': self._y,
        }

    def movement(self, **kwargs) -> dict:   # TODO: incompleted
        # backup
        backup = self.backup()

        # set unknowns
        self._x = sympy.Symbol('x')
        self._y = sympy.Symbol('y')

        # solve equation
        equation = self._equation()
        solution = sympy.solve(equation, self._y, self._x)  # use x to represent y if it can't solve the actual number
        self._solution = solution

        # no solution?
        if not solution:
            self._set(**backup)  # restore
            return {
                'status': 'error',
                'message': 'No solution found'
            }

        # multiple solution?
        if isinstance(solution, list):
            solution = solution[0]

        # completely solved?
        if self._x in solution:
            return {
                'status': 'success',
                'message': 'Solution found',
                'data': {
                    '_x': solution[self._x],
                    '_y': solution[self._y],
                }
            }
        # not solved completely
        else:
            # for 'online', the final solution is: the nearest point on the line
            p = sympy.Point(backup['_x'], backup['_y'])
            l = solution[self._y]
            p = l.projection(p)
            return {
                'status': 'success',
                'message': 'Solution found',
                'data': {
                    '_x': p.x,
                    '_y': p.y,
                }
            }

