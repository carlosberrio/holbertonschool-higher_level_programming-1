#!/usr/bin/python3
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
        """Setter for size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns a key/value argument to attributes"""
        slots = ['id', 'size', 'x', 'y']
        if args:
            """No-keyword argument attributes"""
            for idx, value in enumerate(args):
                if hasattr(self, slots[idx]) and idx < 4:
                    setattr(self, slots[idx], value)
        elif kwargs:
            """Dictionary: key/value attributes"""
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        else:
            return

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        # change this method for something escalable
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
