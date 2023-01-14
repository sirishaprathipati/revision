#Perfect Number=The sum of its divisors is equalto that no.
def Perfectno():
    num=int(input ('Enter a number to check Perfect no or not'))
    s=0
    for i in range(1,num+1//2):
        if num%i==0:
            s=s+i
    if s==num:
        print('It ia a perfect no')
    else:
        print('not a perfect no')
Perfectno()

