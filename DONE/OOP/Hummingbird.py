from DONE.OOP.Apodiformes import Apodiformes


class Hummingbird(Apodiformes):
    def __init__(self, weight, height):
      super().__init__(weight, height)

    def get_food(self):
        print(self.__class__.__name__ + " пьет цветочный нектар и закусывает членистоногими")