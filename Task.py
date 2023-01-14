def Decfun(f):
    
    def inner(li):
       new_li=[]
       for i in li:
            x=str(i)
            new_li.append('+91'+' '+x[-10:-5]+' '+x[-5:])
       return f(new_li)
   
    return inner
@Decfun
def Phnolist(li):
    print(*sorted(li),sep='\n')
li=[int(input())for i in range(int(input('Enter no .of mobile nos:')))]
Phnolist(li)

