import types
class Student :
    def __init__(self,name,age) :
        self.name=name
        self.age=age
        
    def info(self):
        print('Hi'+' '+self.name)

    def Gender(self,gender):
        self.gender=gender
def show_age(self):
    print('Age ',self.age)
obj= Student('raju',20)
obj.info()
obj.Gender('M')
print('gender ',obj.gender)
obj.show=types.MethodType(show_age,obj)
obj.show()
        