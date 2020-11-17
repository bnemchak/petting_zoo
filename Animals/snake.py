from movements.slithering import Slithering
from animals.animals import Animal
from datetime import date

class Snake(Animal, Slithering): 
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
