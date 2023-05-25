import ipdb
from animal import *

class Dog(Animal):

    all = []

    def __init__(self, name, age, bark_volume):
        self.name = name
        self.age = age
        self.bark_volume = bark_volume
        Dog.all.append(self)

    
    def make_animal_sound(self):
        print("Bark!")