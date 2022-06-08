class Bird:

    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height

    def get_weight(self):
        print("Вес " + self.__class__.__name__ + " " + str(self.__weight))

    def get_high(self):
        print("Размер " + self.__class__.__name__ + " " + str(self.__height))

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        print("Цвет " + self.__class__.__name__ + " " + str(self.__color))

    def set_flight_speed(self, speed):
        self.__speed = speed


    def get_flight_speed(self):
        print("Скорость полёта " + self.__class__.__name__ + " " + str(self.__speed))



    def get_food(self):
        print(self.__class__.__name__ + " кушает")
