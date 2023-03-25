from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon character with a given first name."""
        super().__init__(first_name)
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return a string representation of the Baratheon character."""
        return f"{self.family_name}, {self.eyes}, {self.hairs}"

    def __repr__(self):
        """Return a string representation of the Baratheon character."""
        return f"{self.family_name}, {self.eyes}, {self.hairs}"

    def die(self):
        """kill the Lannister character"""
        super().die()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Lannister character with a given first name."""
        super().__init__(first_name)
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return a string representation of the Lannister character."""
        return f"{self.first_name}, {self.family_name}, \
{self.eyes}, {self.hairs}"

    def __repr__(self):
        """Return a string representation of the Lannister character."""
        return f"{self.family_name}, {self.eyes}, {self.hairs}"

    def die(self):
        """kill the Baratheon character"""
        super().die()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool):
        """Create a Lannister character"""
        return cls(first_name, is_alive)
