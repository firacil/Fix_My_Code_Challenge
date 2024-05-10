#!/usr/bin/python3
"""module that provide square implementation"""


class square():
    """class to implement square"""
    width = 0

    def __init__(self, *args, **kwargs):
        """intializing init value"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """permiter of square"""
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """ str of the square"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    """main function to test class"""
    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
