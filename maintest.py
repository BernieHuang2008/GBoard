import sympy
from decimal import Decimal


import xtypes
from relation.relation import GeoRelation


if __name__ == '__main__':
    # Create a point
    point1 = xtypes.X_OBJ_POINT()
    point1._x = Decimal(-4)
    point1._y = Decimal(-2)

    # Create a line
    line1 = xtypes.X_OBJ_LINE()
    line1._k = Decimal(0.5)
    line1._b = Decimal(0)
    # Line2
    line2 = xtypes.X_OBJ_LINE()
    line2._k = Decimal(1)
    line2._b = Decimal(2)

    # Create a relation
    GeoRelation.relate('online', {'target_point': point1.id, 'target_line': line1.id})
    print("[1]", point1.check_relations())
    GeoRelation.relate('online', {'target_point': point1.id, 'target_line': line2.id})
    print("[2]", point1.check_relations())

    # Check the relation
    print("[3]", point1.set(_x=Decimal(1), _y=Decimal(1)))
    print("[4]", point1.check_relations())
    print("[5]", point1._x, point1._y)
