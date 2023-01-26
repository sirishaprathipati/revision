#Acquiring the properties from parent to child class
class parent:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def parent_info(self):
        print('I am '+self.name)
class child(parent):
    def __init__(self,name,age,child_name):
        parent.__init__(self,name,age)
        self.child_name=child_name
    def child_info(self):
        print('I am a child to '+self.name , end='\n'+'my name is'+' '+self.child_name )
obj=child('raju',30,'siva')
obj.child_info()
obj.parent_info()
