#!/bin/usr/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectagle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor
        Args:
            width (int): width of the rectangle
            height (int): length of the rectangle
            x (int): position 'x' of the rectangle
            y (int): position 'y' of the rectangle
            id (int/None): id of the instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for 'x' attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for 'y' attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """Validates width, height, x, and y values"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if name == 'width' or name == 'height':
            if value <= 0:
                raise ValueError('{} must be > 0'.format(name))
        elif name == 'x' or name == 'y':
            if value < 0:
                raise ValueError('{} must be >= 0'.format(name))

    def area(self):
        """Calculates area"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character '#',
        x for 'x axis offset', y for 'y axis offset'"""
        rectangle = '\n' * self.y + \
                    (' ' * self.x + '#' * self.width + '\n') * self.height
        print(rectangle, end='')

    def __str__(self):
        """Returns a string representation of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Calls upd_attr method according arguments pack type"""
        if args:  # can be set with: n, arg in enumerate(args) but DRY
            """No-keyword argument attributes"""
            self.upd_attr(*args)
        elif kwargs:
            """Dictionary: key/value attributes"""
            self.upd_attr(**kwargs)

    def upd_attr(self, id=None, width=0, height=0, x=0, y=0):
        """Updates instance attributes"""
        if id is not None:
            self.id = id
        if width:
            self.width = width
        if height:
            self.height = height
        if x:
            self.x = x
        if y:
            self.y = y

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}
