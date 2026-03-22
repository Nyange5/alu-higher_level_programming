#!/usr/bin/python3
"""Square Class module that defines a Square with size validation."""


class Square:
    """Class that defines a square with validated size."""

    def __init__(self, size=0):
        """Initialize a square with optional size.

        Args:
            size (int): The size of the square (default: 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
