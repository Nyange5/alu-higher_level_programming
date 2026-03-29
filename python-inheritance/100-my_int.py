#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """Rebel int class with inverted == and != operators"""

    def __eq__(self, other):
        """Inverted == operator"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Inverted != operator"""
        return int.__eq__(self, other)
