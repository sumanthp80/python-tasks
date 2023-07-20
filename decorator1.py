'''
Decorators are functions that take another function as an argument 
to modify its behavior without changing the function itself. 
These are useful when we want to dynamically increase the 
functionality of a function without changing it.

Here is an example:
'''
def smart_divide(func):
    def inner(a, b):
        print("Dividing", a, "by", b)
    #    print(func)
        if type(b) != int:
            print("Make sure Denominator is number")
            return
        if b == 0:
            print("Make sure Denominator is non-zero")
            return
        return func(a, b)
    return inner
@smart_divide
def divide(a, b):
    print(a/b)
a=0
#a='a'
#a='0'
divide(1,a)