from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# api_key = app.config['API_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
# @app.route('/random', methods=['GET'])
# def random_cafe():
#     pass


# GET is allowed by default on all routes, so the more simple way is
@app.route('/random')
def random_cafe():
    all_cafe = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafe)
    # return jsonify(cafe={
        # Omit the id from the response
        # "id": random_cafe.id,
        # "name": random_cafe.name,
        # "map_url": random_cafe.map_url,
        # "img_url": random_cafe.img_url,
        # "location": random_cafe.location,
        #
        # # Put some properties in a sub-category
        # "amenities": {
        #     "seats": random_cafe.seats,
        #     "has_toilet": random_cafe.has_toilet,
        #     "has_wifi": random_cafe.has_wifi,
        #     "has_sockets": random_cafe.has_sockets,
        #     "can_take_calls": random_cafe.can_take_calls,
        #     "coffee_price": random_cafe.coffee_price,
        #     }
        # })
    #Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=random_cafe.to_dict())

# all cafes
@app.route('/all')
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


# Search
@app.route('/find')
def find():
    query_location = request.args.get('location')
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at the location"})


## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def create_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={'success': 'Successfully  added the new Cafe.'
                                        ''})


## HTTP PUT/PATCH - Update Record
# PATCH
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={'success': 'Successfully updated the price.'})
    else:
        return jsonify(error={'Not Found': 'Sorry a cafe with that id was not found in the database.'})


## HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def cafe_closed(cafe_id):
    api_key = request.args.get("apy-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={'success': 'Successfully delete the cafe registry from the DB'}), 200
        else:
            return jsonify(error={'Not Found': 'Sorry, a cafe with that id was not found in DB'}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
