# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Woof!"

a = Animal('Buddy')
print(a.speak())

d = Dog('Buddy')
print(d.speak())