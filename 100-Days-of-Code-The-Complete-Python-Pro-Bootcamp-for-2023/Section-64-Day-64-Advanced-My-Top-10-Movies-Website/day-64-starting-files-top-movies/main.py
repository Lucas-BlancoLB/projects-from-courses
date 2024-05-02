import os
import dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

dotenv.load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db = SQLAlchemy(app)


# CREATE TABLE

class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f'Movie {self.title}'


with app.app_context():
    db.create_all()


class EditMovie(FlaskForm):
    rating = StringField("Movie rating 0ut of 10 e.g. 7.6")
    review = StringField("Movie review")
    rank = StringField("Movie rank")
    submit = SubmitField("Submit")


class AddMovie(FlaskForm):
    title = StringField("Movie title:")
    # year = StringField("Year:")
    # description = StringField("Description:")
    # rating = StringField("Rating:")
    # ranking = StringField("Ranking:")
    # review = StringField("Review:")
    # img_url = StringField("A portrait image url:")


# new_movie = Movies(title="Harry Potter and the Sorcerer's Stone", year=2001,
#                    description="Adaptation of the first of J.K. Rowling's popular children's novels about Harry Potter,"
#                                " a boy who learns on his eleventh birthday that he is the orphaned son of two powerful"
#                                " wizards and possesses unique magical powers of his own. He is summoned from his life as"
#                                " an unwanted child to become a student at Hogwarts, an English boarding school for wizards."
#                                " There, he meets several friends who become his closest allies and help him discover the"
#                                " truth about his parents' mysterious deaths.",
#                    rating=8, ranking=10,
#                    review="Magical",
#                    img_url="https://media.themoviedb.org/t/p/w220_and_h330_face/wuMc08IPKEatf9rnMNXvIDxqP4W.jpg")
#
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

# new_movie = Movies(title="The Lord of the Rings: The Return of the King", year="2003",
#                    description="Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from " \
#                                "Frodo and Sam as they approach Mount Doom with the One Ring.",
#                    rating=10, ranking=1,
#                    review="A most watch — an epic fantasy.",
#                    img_url="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/jNN8kQvGVFFdRXb6rZPUD6naqpI.jpg")
#
#
#
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()
@app.route("/")
def home():
    movies = db.session.query(Movies).order_by(desc(Movies.ranking))
    return render_template("index.html", movies=movies)


@app.route("/edit/movie", methods=["POST", "GET"])
def edit():
    id_ = request.args.get("id_")
    movie = db.get_or_404(Movies, id_)
    form = EditMovie(
        rating=movie.rating,
        review=movie.review,
        rank=movie.ranking)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        movie.ranking = int(form.rank.data)

        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route('/delete/<int:id_>')
def delete(id_):
    # id_ = request.args.get("id_")
    movie = db.get_or_404(Movies, id_)
    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for("home"))


@app.route('/add-movie', methods=["POST", "GET"])
def add_movie():
    form = AddMovie()
    if form.validate_on_submit():
        title = form.title.data.strip()
        r = requests.get(os.getenv("URL_API"), params={"api_key": os.getenv("API_KEY"), "query": title}).json()
        data = r['results']
        return render_template("select.html", data=data)
    return render_template("add.html", form=form)

@app.route('/movie-search')
def movie_search():
    TMDB_id = request.args.get("TMDB_id")
    if TMDB_id:
        TMDB_url = f"{os.getenv('URL_API')}/{TMDB_id}"
        data = requests.get(TMDB_url, params={"api_key": os.getenv('API_KEY'), "language": "en-US"}).json()
        new_movie = Movies(title=data["title"], year=data["release_date"].split("-")[0],
                           img_url=f"{TMDB_url}{data['poster_path']}", description=data["overview"])
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))
    else:
        return redirect(url_for("add_movie"))

if __name__ == '__main__':
    app.run(debug=True)
