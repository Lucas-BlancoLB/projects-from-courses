from flask import Flask
# Hello.py v2

def decorator(type_: str):
    type_ = type_.lower()
    if type_ == 'b':
        def bold(funct):
            def wrapper():
                str_ = funct()
                return f'<b>{str_}</b>'
            return wrapper
        return bold
    if type_ == 'em':
        def emphasis(funct):
            def wrapper():
                str_ = funct()
                return f'<em>{str_}</em>'
            return wrapper
        return emphasis
    if type_ == 'u':
        def underlined(funct):
            def wrapper():
                str_ = funct()
                return f'<u>{str_}</u>'
            return wrapper
        return underlined
    else:
        pass


app = Flask(__name__)

print('From Flask:', Flask.__name__)
print(__name__ == '__main__')


@app.route('/')
def hello_world():
    return "<h1 style='text-align: left; color: red'>Hello World</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src='https://media1.tenor.com/m/9SRPROM5RAcAAAAd/kitten-kitty.gif' width=400/>"


@app.route('/bye')
@decorator('b')
@decorator('em')
@decorator('u')
def say_bye():
    return '<h1>Bye</h1>'


@app.route('/bday/<name>/<int:number>')
def bday(name, number):
    return f'<h1>Happy {number}th birthday, {name}!!</h1>'


@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hehe, hii {name}.</h1>'


@app.route('/greets/<path:name>')
def greets(name):
    return f'<h1>Hehe, hii {name}.</h1>'


@app.route('/num/<int:n>')
def num(n):
    return f'<h1>Is your favorite number {n}?</h1>'


if __name__ == '__main__':
    app.run(debug=True)

''''
## ********Day 54 Start**********
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function()


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()

'''
