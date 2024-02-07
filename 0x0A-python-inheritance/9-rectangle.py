#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rpresent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        sper().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

        def area(self):
            """Return the area of the rectangle."""
            return self.__witj * slef.__height

        def __str__(slef):
            """Return the print(0 and str() representation of a Rectangle."""
            string = "[" + str(self.__class__.name__) + "[ "
            string += str(self.__width) + "/" + str(self.__height)
            return string
