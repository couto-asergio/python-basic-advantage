from datetime import datetime
from random import randint


class Person:
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, eating=False, talking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking

    def talk(self, subject):
        if self.eating:
            print(f"{self.name} don't talking eating.")
            return

        if self.talking:
            print(f'{self.name} is already talking.')

        print(f'{self.name} is talking about {subject}.')

    def stop_talking(self):
        if not self.talking:
            print(f'{self.name} is not talking.')
            return

        print(f'{self.name} stopped talking.')
        self.falando = False

    def eat(self, food):
        if self.eating:
            print(f'{self.name} is already eating.')
            return

        if self.talking:
            print(f"{self.name} don't eat talking.")
            return

        print(f'{self.name} is eating {food}.')
        self.eating = True

    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is not eating.')
            return

        print(f'{self.name} stopped eating.')
        self.comendo = False

    def get_year_birth(self):
        return self.current_year - self.age

    # 100. Métodos de classes - Python Orientado a Objetos
    # Decorator Method
    @classmethod
    def by_year_birth(cls, name, year_birth):
        age = cls.current_year - year_birth
        return cls(name, age)

    # 100. Métodos de classes - Python Orientado a Objetos
    # Decorator Method
    @staticmethod
    def generation_id():
        rand = randint(100000, 19999)
        return rand
