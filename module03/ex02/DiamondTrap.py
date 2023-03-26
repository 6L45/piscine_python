from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    A class representing a King.
    """
    def __init__(self, first_name):
        """
        Initializes the King instance
        the __init__() method of the super classes.
        """
        super().__init__(first_name)

    @property
    def name(self):
        """
        Returns the name of the class.
        """
        return self.__class__.name

    @name.setter
    def name(self, value):
        """
        Sets the name of the class.
        """
        self.__class__.name = value

    def get_eyes(self):
        """
        Returns the color of the King's eyes.
        """
        return self.eyes

    def get_hairs(self):
        """
        Returns the color of the King's hair.
        """
        return self.hairs

    def set_eyes(self, color):
        """
        Sets the color of the King's eyes.
        """
        self.eyes = color

    def set_hairs(self, color):
        """
        Sets the color of the King's hair.
        """
        self.hairs = color
