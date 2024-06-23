from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date, datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type :
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class NewPost(FlaskForm):
    title = StringField("Post Title", validators=[DataRequired()])
    subtitle = StringField("Post Subtitle", validators=[DataRequired()])
    author = StringField("Author's name", validators=[DataRequired()])
    img_url = StringField("Blog Post Image-URL", validators=[DataRequired()])
    text = CKEditorField("Post Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

@app.context_processor
def current_year():
    return {'current_year': datetime.now().year}


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = [x for x in db.session.query(BlogPost)]
    print(posts)
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/<post_id>')
def show_post(post_id):

    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.get(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = NewPost()
    if form.validate_on_submit():
        new_post = BlogPost(title=form.title.data.strip(),
                            subtitle=form.subtitle.data.strip(),
                            date=datetime.now().strftime("%B %d, %Y"),
                            author=form.author.data.strip(),
                            img_url=form.img_url.data.strip(),
                            body=form.text.data.strip())
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, title="New Post")

# TODO: edit_post() to change an existing blog post
@app.route("/edit/<int:post_id>", methods=["GET","POST"])
def edit_post(post_id):
    r_post = db.session.get(BlogPost, post_id)
    form = NewPost(title=r_post.title,subtitle=r_post.subtitle, author=r_post.author,
                   img_url=r_post.img_url, text=r_post.body)
    if form.validate_on_submit():
        r_post.title, r_post.subtitle = form.title.data.strip(), form.subtitle.data.strip()
        r_post.author, r_post.img_url = form.author.data.strip(), form.img_url.data.strip()
        r_post.body = form.text.data.strip()
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, title="Edit Post")

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete(post_id):
    r_post = db.session.get(BlogPost, post_id)
    db.session.delete(r_post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
