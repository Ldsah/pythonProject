from DONE.OOP.Apodiformes import Apodiformes
from DONE.OOP.Bird import Bird
from DONE.OOP.Hummingbird import Hummingbird
from DONE.OOP.Swift import Swift

bird = Bird(2, 10)
birdA = Apodiformes(15, 3)
birdS = Swift(11, 7)
birdH = Hummingbird(7, 3)

bird.get_high()
birdA.get_high()
birdS.get_high()
birdH.get_high()

bird.get_food()
birdA.get_food()
birdS.get_food()
birdH.get_food()