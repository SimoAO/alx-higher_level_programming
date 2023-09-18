#!/usr/bin/python3
"""The Square class module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class named Square that inherits
    from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of Square"""
        return"[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Returns the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns a key/value argument to attributes"""
        attrs = ["id", "size", "x", "y"]
        attrs_v = []
        if not args or args is None:
            for attrs, attrs_v in kwargs.items():
                setattr(self, attrs, attrs_v)
        else:
            for value in args:
                attrs_v.append(value)
                for i range(len(attrs_v)):
                setattr(self, attrs[i], attrs_v[i])

    def to_dictionary(self):
        """Returns the dictionary representation of the Square"""
        return {"id": self.id, "size": self.size, "x": self.x,
                "y": self.y}
