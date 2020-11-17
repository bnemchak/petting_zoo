from attractions.attraction import Attraction

class Amazon(Attraction):
    def __init__(self, attraction_name, description):
        super().__init__(attraction_name, description)

    def add_animal(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f"{animal} can be found in {self.attraction_name}")
        except AttributeError as ex:
            print(f"{animal} does not belong in {self.attraction_name}")
