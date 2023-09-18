#!/usr/bin/python3
"""The Rectangle class module"""


from models.base import Base


class Rectangle(Base):
    """A class named Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for row in range(self.__y):
            print("\n", end="")
        for row in range(self.__height):
            for column in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns the string representation of the Rectangle"""
        return"[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns a key/value argument to attributes"""
        attrs = ["id", "width", "height", "x", "y"]
        attrs_v = []

        if not args or args is None:
            for attrs, attrs_v in kwargs.items():
                setattr(self, attrs, attrs_v)
        else:
            for value in args:
                attrs_v.append(value)
                for i in range(len(attrs_v)):
                setattr(self, attrs[i], attrs_v[i])

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
