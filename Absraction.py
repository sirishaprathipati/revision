# Hiding something from outside world
from abc import ABC,abstractmethod 
class Animal(ABC):
    @ abstractmethod
    def sounds(self):
        pass
class Dog(Animal):
    def sounds(self):
        print('bow bow')

class cat(Animal):
    def sounds(self):
        print('meow meow')
D=Dog()
D.sounds()
c=cat()
c.sounds()