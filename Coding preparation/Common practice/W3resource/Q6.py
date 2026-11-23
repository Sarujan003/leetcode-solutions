# Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return self.side * self.side

s = Square(4)

print(s.area())