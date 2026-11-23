# Polymorphism

class Cat:
    def __init__(self):
        pass

    def sound(self):
        return "Meow"

class Duck:
    def __init__(self):
        pass

    def sound(self):
        return "Quack"

def animal_sound(animal_object):
    print(animal_object.sound())

c = Cat()
d = Duck()

for obj in [c,d]:
    animal_sound(obj)