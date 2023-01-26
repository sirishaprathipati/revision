class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def P_info(self):
        print(self.name)
class Employee(person):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id=id
    def E_info(self):
        print('I am from '+self.__class__.__name__+' class')
        print(self.id)
class Manager(Employee,person):
    def __init__(self,name,age,id ,rights):
        super().__init__(name, age,id)
        self.rights=rights
    def M_info(self):
        print(self.rights)

obj=Manager('Sirisha',27,1,'Manager')
obj.E_info()
obj.P_info()
obj.M_info()
