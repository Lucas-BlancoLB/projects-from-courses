from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)
# Create database
class Base(DeclarativeBase):
  pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)

# Initialise the app with the extension
db.init_app(app)


# Create table
class Book(db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
  author: Mapped[str] = mapped_column(String, nullable=False)
  rating: Mapped[float] = mapped_column(Float, nullable=False)

  # Optional: this will allow each book object to be identified by its title when printed.
  def __repr__(self):
    return f'<Book {self.title}'



# Create table schema in the database. Requires application context.
with app.app_context():
  db.create_all()

# CREATE RECORD
with app.app_context():
  new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=7.6)
  db.session.add(new_book)
  db.session.commit()












# import sqlite3
#
#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, "
# #                "title varchar(250) NOT NULL UNIQUE, "
# #                "author varchar(250) NOT NULL, "
# #                "rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '7.6')")
# db.commit()