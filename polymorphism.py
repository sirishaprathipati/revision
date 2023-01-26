# A piece of code behaving differently in different situation
class Dog:
    def sounds(self):
        print('Bow Bow')
class cat:
    def sounds(self):
        print('Meow Meow')

def calling(obj):
    obj.sounds()

D=Dog()
C=cat()
for pet in (D,C):
    pet.sounds()
