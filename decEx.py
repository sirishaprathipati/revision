def DecFun (f):
    def inner(x,y):
        if y==0:
            print('we cannt divide ')
        else:
            f()
    return inner
@DecFun
def divide(x,y):
    x=int(input('Enter a value'))
    y=int(input('Enter a value'))
    c=x/y
    print(c)
    