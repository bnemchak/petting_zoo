from movements.walking import Walking
from animals.animals import Animal
from datetime import date

class Hedgehog(Animal, Walking): 
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
