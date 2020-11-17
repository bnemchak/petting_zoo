from movements.walking import Walking
from animals.animals import Animal
from datetime import date

class Llama(Animal, Walking): 
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
