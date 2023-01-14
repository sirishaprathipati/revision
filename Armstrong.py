# Armstrong number=the sum of nth power of each digit to a n digit number is equal to that number

def Armstrong(ch):
    num=str(ch)
    sum=0
    for i in range(0,len(num)):
        base=int(num[i])
        power=len(num)
        sum=sum+pow(base,power)
    if sum==ch:
        print(sum)

for j in range(10,2000):
    Armstrong(j)
