from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, exc
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def create_dict(self):
        return [{column.name: getattr(obj, column.name) for column in obj.__table__.columns} for obj in self]

    def error_not_found(loc):
        return {'Not Found': f"Sorry, we don't have a cafe at {loc} location."}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random_table():
    cafe_num = db.session.query(Cafe).count()
    random_cafe = random.randint(1, cafe_num)
    row = db.session.query(Cafe).get(random_cafe)
    row = [row]
    print(row)
    return jsonify(cafe=Cafe.create_dict(row))


@app.route("/all")
def all_cafe():
    cafe = db.session.query(Cafe).all()
    print(cafe)
    return jsonify(cafe=Cafe.create_dict(cafe))


@app.route("/search")
def search():
    loc = request.args.get('loc')
    cafe = db.session.query(Cafe).all()
    cafe = [cafe_ for cafe_ in cafe if cafe_.location == loc]
    print(cafe)

    return jsonify(cafe=Cafe.create_dict(cafe)) if cafe else jsonify(error=Cafe.error_not_found(loc)), 404


# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('loc'),
        has_sockets=bool(request.form.get('sockets')),
        has_toilet=bool(request.form.get('toilet')),
        has_wifi=bool(request.form.get('wifi')),
        can_take_calls=bool(request.form.get('calls')),
        seats=request.form.get('seats'),
        coffee_price=request.form.get('coffee_price'), )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/edit-price/<int:cafe_id>", methods=["PATCH"])
def patch_cafe(cafe_id):
    cafe_price = request.args.get("cafe_price")
    if not cafe_price:
        return jsonify(error={"something wrong": "try to  '/edit-price/CAFE_ID?cafe_price=PRICE'"})
    try:
        cafe = db.session.query(Cafe).filter_by(id=cafe_id).one()
        cafe.coffee_price = cafe_price
        db.session.commit()
        return jsonify(response={"success": f"Successfully updated the cafe's price to '{cafe_price}'."}), 200

    except exc.NoResultFound:
        return jsonify(error={"Not found": f"No cafe with '{cafe_id}' id.",
                              "Tip": 'the id most be an int, within db range.'}), 404



# HTTP DELETE - Delete Record
@app.route("/remove-cafe/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get('API-KEY')
    if api_key == 'TopSecretAPIKey':
        try:
            cafe = db.session.query(Cafe).filter_by(id=cafe_id).one()
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        except exc.NoResultFound:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
