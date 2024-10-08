from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, AnonymousUserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from datetime import datetime as dt
'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
login_manager = LoginManager()
ckeditor = CKEditor(app)
Bootstrap5(app)
login_manager.init_app(app)


# TODO: Configure Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(250), unique=True, nullable=False)
    subtitle = db.Column(String(250), nullable=False)
    date = db.Column(String(250), nullable=False)
    body = db.Column(Text, nullable=False)
    img_url = db.Column(String(250), nullable=False)

    user_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")

    comments = relationship("Comment", back_populates="parent_post")


# TODO: Create a User table for all your registered users. 
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    name = db.Column(db.String())

    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")


with app.app_context():

    db.create_all()


@app.context_processor
def context():
    return {"current_year": dt.now().year}

def wrapped(f):
    @wraps(f)
    def admin(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)

        return f(*args, **kwargs)

    return admin


gravatar = Gravatar(app, size=100, rating='g', default='retro',
                    force_default=False, force_lower=False,
                    use_ssl=False, base_url=None)


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if not User.query.filter_by(email=form.email.data).first():
            hash_ = generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=18)
            new_user = User(email=form.email.data, password=hash_, name=form.name.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("get_all_posts"))
        else:
            flash("Email already registered. Please log in.")
            return redirect(url_for("login"))
    return render_template("register.html", form=form)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("get_all_posts"))
        else:
            flash("Email or password is wrong.")
            return redirect(url_for("login"))
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if current_user.is_anonymous:
            flash("You must be logged to comment.")
            return redirect(url_for('login'))
        new_comment = Comment(text=comment_form.body.data.strip(),
                              parent_post=requested_post,
                              comment_author=current_user)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
        # comments = Comment.query.filter_by(author_id=author_id.id).all()
    return render_template("post.html", post=requested_post, form=comment_form, current_user=current_user)


# TODO: Use a decorator so only an admin user can create a new post

@app.route("/new-post", methods=["GET", "POST"])
@wrapped
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@wrapped
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post

@app.route("/delete/<int:post_id>")
@wrapped
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
