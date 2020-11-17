from movements.slithering import Slithering
from movements.walking import Walking
from animals.animals import Animal
from datetime import date

class Lizard(Animal, Slithering, Walking): 
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        Walking.__init__(self)
