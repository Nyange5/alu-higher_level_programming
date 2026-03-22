#!/usr/bin/python3
"""Square Class.
Module that defines a Square Class with private size attribute"""


class Square:
    """Class that defines a square with private size.
    Attribute:
        size: Integer indicating the size of the square object."""

    def __init__(self, size):
        """An object constructor method.
        Initialize a square with given size.

        Args:
            size: Integer indicating object size
        """
        self.__size = size
