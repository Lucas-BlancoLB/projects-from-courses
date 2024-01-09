def add(*args):
    # args are tuple u can use index
    print(args[0])
    print(type(args))
    print(sum(args))


add(1, 2, 6, 1, 1232, 45)


def calculate(n, **kwargs):
    # kwargs means keywords_arguments
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
    print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # get returns None if the value isn't defined
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.make, my_car.model)