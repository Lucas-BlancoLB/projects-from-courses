from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post_data = Post()
@app.route('/')
def home():

    return render_template("index.html", data=post_data.r)

@app.route('/post<int:blog_id>')
def blog(blog_id):
    print(blog_id)
    return render_template('post.html', blog_id=blog_id, data=post_data.r)
if __name__ == "__main__":
    app.run(debug=True)
