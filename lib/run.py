import ipdb
from animal import *
from dog import *
from cat import *

animal1 = Animal("Fluffy", 4)
animal2 = Animal("Kitty", 2)

dog1 = Dog("Fido", 13)


Animal.get_all_animal_names()

ipdb.set_trace()