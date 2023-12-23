import session

import random

random.seed(0x585858)


def ID():
    id = str(random.random())
    while id in session.OBJECTS or id in session.RELATIONS:
        id = str(random.random())
    return id

