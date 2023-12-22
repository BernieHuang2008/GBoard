import sympy
from decimal import Decimal


import xtypes
from relation.relation import GeoRelation


if __name__ == '__main__':
    # Create a point
    point1 = xtypes.X_OBJ_POINT()
    point1._x = Decimal(2)
    point1._y = Decimal(1)
    # Create a line
    line1 = xtypes.X_OBJ_LINE()
    line1._k = Decimal(0.5)
    line1._b = Decimal(0)
    # Create a relation
    rel1 = GeoRelation.from_preset('online', {'target_point': point1.id, 'target_line': line1.id})
    print(rel1.check())
