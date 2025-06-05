from dataclasses import dataclass, field
from libops.random_utilities import RandomUtilities

@dataclass(frozen=True, order=True, slots=True)
class Book:
    title: str
    author: str
    genre: str
    _value: float = 0.0
    isbn: str = field(default_factory=RandomUtilities.generate_ISBN)

    @property
    def value(self):
        return round(self._value, 2)

    @property
    def search_string(self):
        return f"{self.title} {self.genre}"
