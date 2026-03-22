#!/usr/bin/python3
"""Square Class.
Module that defines a Square Class with size validation
"""


class Square:
    """Class that defines a square with validated size"""

    def __init__(self, size=0):
        """Initialize a square with optional size

        Args:
            size: The size of the square (default: 0)

        Raises:
            ValueError: If size < 0.
            TypeError: If size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
