#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base(12)
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base()
    print(b4.id)

    b5 = Base()
    print(b5.id)

    b6 = Base()
    print(b6.id)

    b7 = Base('Hola')
    print(b7.id)

    print(type(b7))