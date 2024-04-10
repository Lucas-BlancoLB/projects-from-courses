from flask import  Flask, render_template
import random
import datetime as dt
import requests
app = Flask(__name__)

@app.route('/')
def home():

    random_num = random.randint(0, 100)
    current_year = dt.datetime.now().year
    return render_template('index.html', N=random_num, year=current_year)

@app.route('/guess/<name>')
def guess(name : str):
    if name.isalpha():
        r1 = requests.get(f'https://api.genderize.io/?name={name}').json()
        r2 = requests.get(f'https://api.agify.io/?name={name}').json()
        return render_template('guess.html', name=name.capitalize(), gender=r1['gender'], years_old=r2['age'])
    else:
        return '<title>Error</title>' \
               '<h1>wrong input</h1>' \
               '<h2>put a name after ->  "/guess/"</h2>'


@app.route('/blog/<int:num>')
def blog_(num):
    r_dict = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    print(r_dict)
    return render_template('blog.html', data=r_dict, num=num)


if __name__ == '__main__':
    app.run(debug=True)