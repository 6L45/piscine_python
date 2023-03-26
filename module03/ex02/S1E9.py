from abc import ABC, abstractmethod


class Character(ABC):
    """
        astract base class for characters in Game of Thrones
    """

    def __init__(self, first_name: str):
        """
            Initialize a Character instance with a given first name
        """
        self.first_name = first_name
        self.is_alive = True

    @abstractmethod
    def die(self):
        """
            Kill the character
        """
        self.is_alive = False


class Stark(Character):
    """Class representing the Stark family in Game of Thrones"""

    def __init__(self, first_name: str):
        """Initialize a Stark instance with a given first name"""
        super().__init__(first_name)

    def die(self):
        """Kill the Stark by setting is_alive attribute to False"""
        super().die()
