class Tvarina:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "ця тварина робить"

    def info(self):
        return f"поганяло на зоні: {self.name}, срок: {self.age} років"

class Sobaka(Tvarina):
    def make_sound(self):
        return "гау"

class Kit(Tvarina):
    def make_sound(self):
        return "мяу мяу йопта"

sobaka = Sobaka("патрон", 3)
kit = Kit("нефар", 2)

print(sobaka.info())
print(sobaka.make_sound())

print(kit.info())
print(kit.make_sound())