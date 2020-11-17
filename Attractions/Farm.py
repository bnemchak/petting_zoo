from attractions.attraction import Attraction

class Farm(Attraction):
    def __init__(self,attraction_name,description):
        super().__init__(attraction_name, description)

    def add_animal(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal} lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f"{animal} doesn't go in {self.attraction_name}")
