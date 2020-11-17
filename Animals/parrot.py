from movements.flying import Flying
from animals.animals import Animal
from datetime import date

class Parrot(Animal, Flying): 
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Flying.__init__(self)
