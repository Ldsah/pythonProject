# стрижеобразные
from DONE.OOP.Bird import Bird


class Apodiformes(Bird):
    def __init__(self, weight, height):
        super().__init__(weight, height)
        print(self.__class__.__name__)

    def get_food(self):
        print(self.__class__.__name__ + " питаются членистоногими или цветочным нектаром")
