import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random ID consisting of 15 lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A class representing a student"""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Initialize the login attribute
        to the capitalized surname after object creation."""
        self.login = self.surname.capitalize()
