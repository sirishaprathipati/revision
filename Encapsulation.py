#Wrapping up of data(variables and methids into a single entity)
class A:
    def __init__(self,name):
        self.name=name # -------------  (Public variables)        
    def display(self):
        print(self.name)
obj1=A('Siri')
#obj1.display()
print(obj1.name)




class B:
    def __init__(self,name):
        self.__name=name  #--------------(private variables)
    def display(self):
        print(self.__name)
obj2=B('Nithya')
obj2.display()
#print(obj2._B.__name) #-----------------(we cann't access from outside,we get error)

class C:
    def __init__(self,name):
        self._name=name
    def display(self):
        print(self._name)
obj3=C('Dhanya')
#obj3.display()
print(obj3._name) #------------------------(we can access from outside)
