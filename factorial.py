ch=int(input('Enter a Number to find Factorial:'))
def factorial(num):
    f=1
    if num>0:
        for i in range(1,num+1):
            f=f*i
        print(f)
    else :
        print('Please Enter correct input')

factorial(ch)
