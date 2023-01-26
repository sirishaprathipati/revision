class A:
    def display(self):
        print('Iam from class A')
class B(A):
    #pass
    def display(self):
        print('Iam from class B')
obj=B()
obj.display()
print(B.mro())

    