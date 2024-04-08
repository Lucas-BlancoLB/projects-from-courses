from flask import Flask
from random import randint

random_num = randint(0, 9)
app = Flask(__name__)


def result(*args):
    if args[0] < random_num:
        str_ = "<em><b><h1 style='text-align: center'>Too low, try again!</h1></b></em>" \
               "<img style='display: block; margin: 0 auto;' " \
               "src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
        return str_
    elif args[0] > random_num:
        str_ = "<em><b><h1 style='text-align: center'>Too high, try again!</h1></b></em>" \
               "<img style='display: block; margin: 0 auto;' " \
               "src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
        return str_
    else:
        str_ = "<em><b><h1 style='text-align: center'>You found me!</h1></b></em>" \
               "<img style='display: block; margin: 0 auto;' " \
               "src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
        return str_


@app.route('/')
def home():
    return "<em><b><h1 style='text-align: center'>Guess a number between 0 and 9</h1></b></em>" \
           "<img style='display: block; margin: 0 auto;' " \
           "src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route('/<int:n>')
def game(n):
    return result(n)


if __name__ == '__main__':
    app.run(debug=True)
