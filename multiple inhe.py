class A:
    def diplay(self):
        print("Super Class 1 method called")

class B:
    def info(self):
        print("Super Class 2 method called")

class C(A, B):
    pass
    #def info(self):
     #   print("Super Class 3 method called")


d1 = C()
d1.diplay()  