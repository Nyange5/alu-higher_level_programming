#!/usr/bin/python3
"""Square Class module that defines a Square with size validation."""


class Square:
    """Class that defines a square with validated size."""

    def __init__(self, size=0):
        """Initialize a square with optional size.

        Args:
            size (int): The size of the square (default: 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
