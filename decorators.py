def decFun(fn):
    def inner():
        print('*****************')
        fn()
        print('*****************')
    inner()
@decFun
def display():
    print('Hello Display')
