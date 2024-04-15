from flask import Flask, render_template
from post_request import Data
from datetime import datetime as dt
import random
post_data = Data().r  # .r to get only the data
post_data_len = len(post_data)
date = dt.now().strftime("%B %d, %Y")
random_index = random.randrange(0, len(post_data))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", post_data=post_data, date=date, sample_post=random_index, len=post_data_len)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post_pg/<int:index_id>')
def post_pg(index_id):
    print(type(index_id), index_id)
    post = post_data[int(index_id)]
    return render_template("post_pg.html", post=post)


@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)