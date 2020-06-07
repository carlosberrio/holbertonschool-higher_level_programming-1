#!/bin/usr/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor
        Args:
            size (int): width/length of the square
            x (int): position 'x' of the square
            y (int): position 'y' of the square
            id (int/None): id of the square's instance
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter for size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """Calls upd_attr method according arguments pack type"""
        if args:
            """No-keyword argument attributes"""
            self.upd_attr(*args)
        elif kwargs:
            """Dictionary: key/value attributes"""
            self.upd_attr(**kwargs)

    def upd_attr(self, id=None, size=0, x=0, y=0):
        """Updates instance attributes"""
        if id is not None:
            self.id = id
        if size:
            self.size = size
        if x:
            self.x = x
        if y:
            self.y = y

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
