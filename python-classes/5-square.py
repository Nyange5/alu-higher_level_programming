#!/usr/bin/python3
"""Square Class.
Module contains a class that defines a square."""

class Square:
    """class that defines a square"""

    def __init__(self, size=0):
        """Initialize square with size.
        Args:
            size: integer representing object size."""

        self.size = size


    @property
    def size(self):
        """Getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculation of the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Shows the square object with # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size) 
