#pallendrome= The reverse of a given no is equlAL to thal number(121,1001)
num=int(input('Enter a Number '))
s=0
bkp=num
while num>0:
    digit=num%10
    s=s*10+digit  
    num=num//10
#print(s)
if s==bkp:
    print('The given no is pallendrome')
else:
    print('not a pallendrome')