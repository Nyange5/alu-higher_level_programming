#!/usr/bin/python3
"""Square Class.
Module contains a class that defines a square.
"""


class Square:
    """This class defines a square with size and position"""

    def __init__(self, size=o, position=(0, 0)):
         """Initialize a square with optional size and position
        Args:
            size: The size of the square (default: 0)
            position: The position of the square (default: (0, 0))
        """
        self.size = size
        self.position position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square with validation
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
            """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square with validation.
        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """print the square with # characters at given position"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
