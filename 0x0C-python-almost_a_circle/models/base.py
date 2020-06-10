#!/usr/bin/python3
"""Module for Base Class"""
from json import dumps, loads
from os import path
import csv


class Base:
    """Defines a Base class
        __nb_objects (int): counter of active instances and <id> for instances
        with no setted id, default = None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor - Sets id attribute to all future instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of
        <list_dictionaries>: the dictionary representation of a instance
        dumps(): Dict Python to JSON"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON str representation <json_string>
        Loads(): JSON to Python Dict"""
        if json_string is None or not json_string:
            return []
        else:
            return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of <list_objs> to a file"""
        file = "{}.json".format(cls.__name__)
        dics_list = []
        if list_objs is not None:
            dics_list = [obj.to_dictionary() for obj in list_objs]
        with open(file, 'w', encoding='utf-8') as jsonfile:
            jsonfile.write(cls.to_json_string(dics_list))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
            cls: cls argument to access to the class, instead of calling
                 the constructor directly
            (kwargs) dictionary: attributes to set
            To use the update method to assign all attributes, a “dummy”
            instance is created"""
        dummy = cls(3, 2) if cls.__name__ == "Rectangle" else cls(5)
        # 2 are the minimum positional arguments for rect, 1 for square
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Creates a <class-name.json> file, check content, loads it as a
        Python list of dictionaries, creates instances with every dictionary
        and returns the list of instances"""
        file = "{}.json".format(cls.__name__)
        if path.exists(file):  # os Module
            with open(file, 'r', encoding='utf-8') as jsonfile:
                inst_dicts = cls.from_json_string(jsonfile.read())
                inst_list = [cls.create(**dic) for dic in inst_dicts]
                return inst_list
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of Rectangles/Squares objects
        Args:
            List of squares or Rectangle instances
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[ob.id, ob.width, ob.height, ob.x, ob.y]
                             for ob in list_objs]
            else:
                list_objs = [[ob.id, ob.size, ob.x, ob.y]
                             for ob in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of Rectangles/Squares in csv
        Returns:
            is file is None or empty, return an empty list
            Otherwise, a list of instances
        """
        from models.rectangle import Rectangle
        from models.square import Square
        inst_list = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    dic = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    dic = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                inst_list.append(cls.create(**dic))
        return inst_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares
        using the Turtle graphics module"""
        import turtle
        from time import sleep
        from random import randrange, choice
        turtle.getscreen()
        turtle.bgcolor("black")
        turtle.Screen().colormode(255)
        t = turtle.Turtle()
        shapes = ["arrow", "turtle", "classic"]
        for figure in list_rectangles + list_squares:
            t.shape(choice(shapes))
            R = randrange(0, 257, 10)
            G = randrange(0, 257, 10)
            B = randrange(0, 257, 10)
            t.setpos(
                figure.x - 150 + randrange(0, 100),
                -75 + figure.y + randrange(0, 100))
            t.speed(1)
            t.fillcolor(R, G, B)
            t.pencolor('black')  # line color
            t.begin_fill()
            t.forward(figure.width)
            t.left(90)
            t.forward(figure.height)
            t.left(90)
            t.forward(figure.width)
            t.left(90)
            t.forward(figure.height)
            t.left(90)
            t.end_fill()
            sleep(3)
            t.clear()
