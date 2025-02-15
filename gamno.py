import random

class Dog:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.energy = 50
        self.alive = True

    def to_eat(self):
        print('пес хаває')
        self.happiness += 5
        self.energy += 10

    def to_sleep(self):
        print('пес дрихне(не здох(мб))')
        self.energy += 15
        self.happiness += 3

    def to_play(self):
        print('грається з банкою квашених помідорів')
        self.happiness += 7
        self.energy -= 5

    def is_alive(self):
        if self.energy <= 0:
            print('стомлений звер капец')
            self.alive = False
        elif self.happiness <= 0:
            print('втх собака дед інсайд💀')
            self.alive = False
        elif self.happiness > 100:
            print('собака занадто рада, ніби нанюхалась')
            self.happiness = 100

    def end_of_day(self):
        print(f'Щастя = {self.happiness}')
        print(f'енергія(тіпа те шо в мене немає) = {self.energy}')

    def live(self, day):
        day = 'день ' + str(day) + ' of ' + self.name + ' life'
        print(f'{day:=^50}')

        life_event = random.randint(1, 3)
        if life_event == 1:
            self.to_eat()
        elif life_event == 2:
            self.to_sleep()
        elif life_event == 3:
            self.to_play()

        self.end_of_day()
        self.is_alive()

rex = Dog(name='патрон')

for day in range(365):
    if not rex.alive:
        break
    rex.live(day)