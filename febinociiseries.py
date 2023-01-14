# Each number is the sum of two proceeding numbers
ch=int(input('Enter a Number for febinocii series:'))

def febinocii(num):
    x=0
    y=1
    
    for i in range(1,num+1):
        z=x+y
        print(z,end='   ')
        x=y
        y=z
febinocii(ch)