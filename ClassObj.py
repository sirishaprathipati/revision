class Calc:
     def __init__(self,a,b) :
          self.num1=a
          self.num2=b
     def Addition(self):
            c=self.num1+self.num2
            print(c)
     def Substraction(self):
        if self.num1>self.num2:
            c=self.num1-self.num2
            print(c)
        else :
            c=self.num2-self.num1
            print(c)

obj1=Calc(10,20)
obj1.Addition()
obj1.Substraction()

