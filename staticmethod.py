class Person:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
    @staticmethod
    def is_Young(age):
        if age<30:
            return True
        else:
            return False
obj=Person('raju',36)
obj.info()
print(obj.is_Young(28))