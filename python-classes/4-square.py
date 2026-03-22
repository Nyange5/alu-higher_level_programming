#!/usr/bin/python3

"""Square Class.
Module that defines a Square class with getter and setter
"""


class Square:
     """Defines a square with size and area calculation."""

     def __init__(self, size=0):
         self.size = size

    @property
    def size(self):
        """return new size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation

        Args:
            value: The size value to set

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
