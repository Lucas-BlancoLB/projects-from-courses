inputs = [1, 2, 3]


# TODO: Create the logging_decorator() function 👇
def logging_decorator(funct):
    def wrapped(*args):
        print(f'You called {funct.__name__}{args}')
        print(f'It returned: {funct(*args)}')
    return wrapped


# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
