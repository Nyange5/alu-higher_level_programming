#!/usr/bin/python3
"""Square Class.
Module that defines a Square class with area calculation"""


class Square:
    """Class that defines a square with area calculation"""

    def __init__(self, size=0):
        """Initialize a square with optional size

        Args:
            size: The size of the square (default: 0)"""
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """Return the new area of the square."""
        return (self.__size * self.__size)
