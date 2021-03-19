# Advance arguments arg and **kw, we can use any word after the *


def add(*args):#->unlimited arguments
    sum = 0
    print(type(args))
    for n in args:
        sum += n
    return sum


print(add(8, 7, 5, 6))

def calculate(n, **kwargs):# unlimited key=value
    print(type(kwargs))
    print(kwargs)
    for (key, value) in kwargs.items(): #->need the .items() method to iterate the dict
        print(key)
        print(value)
    print(kwargs["add"])
    n += kwargs["add"]
    n /= kwargs["division"]
    print(n)


calculate(2, add=5, division=3)#->return a dictionarie

class Car():
    def __init__(self, **kw):
        self.make  = kw["make"]#->when we run the class, we need specify the 2 arguments
        self.model = kw["model"]#->

my_car = Car(make="Ford", model="Mustang")
print(my_car.model)

class Car2():
    def __init__(self, **kw):
        self.make  = kw.get("make")#->when we use the .get() arguments are optionals
        self.model = kw.get("model")#->

my_car2 = Car2(model="Mustang")
print(my_car2.model)
print(my_car2.make)