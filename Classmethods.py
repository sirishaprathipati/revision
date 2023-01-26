class Student:
    College_name='ABC College'
    def __init__(self,name) :
        self.name=name
    def info(self):
        print(self.name,Student.College_name)
    #@classmethod
    #def c_name(cls,cname):
     #   cls.College_name=cname
      #  print(cls.College_name)
def c_name(cls,cname):
    cls.College_name=cname
    print(cls.College_name)
    
Student.c_name=classmethod(c_name)

obj=Student('Raju')
obj.info()
#obj.c_name('XYZ college')
print(Student.College_name)
obj.c_name('123 School')
print(Student.College_name)
