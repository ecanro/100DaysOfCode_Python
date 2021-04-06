from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import requests, os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
DB_URI = 'sqlite:///movies-collection.db'

# Create DB
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# silence warnings in the console
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create Table
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    #optional:allow each movie object to be identified by title
    def __repr__(self):
        return f'<Book {self.title}>'

# This code must come _after_ the class definition
if not os.path.isfile(DB_URI):
    db.create_all()

# creating a new register(only for code purposes)
# new_movie = Movies(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


# Add form
class AddForm(FlaskForm):
    title = StringField('Title', _name='title', validators=[DataRequired()])
    year = StringField('Year', _name='year', validators=[DataRequired()])
    description = StringField('Description', _name='description', validators=[DataRequired()])
    rating = StringField('Rating', _name='rating', validators=[DataRequired()])
    ranking = StringField('Ranking', _name='ranking', validators=[DataRequired()])
    review = StringField('Review', _name='review', validators=[DataRequired()])
    img_url = StringField('Title', _name='url', validators=[DataRequired(), URL()])
    submit = SubmitField('Done')


# edit form
class UpdateForm(FlaskForm):
    ranking = StringField('Your rating out of 10, eg.: 9.5:', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

# home
@app.route("/")
def home():
    # Read
    all_movies = db.session.query(Movies)
    return render_template("index.html", movies=all_movies)


# add
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if request.method == 'POST':
        new_movie = Movies(
            title=request.form['title'],
            year=request.form['year'],
            description=request.form['description'],
            rating=request.form['rating'],
            ranking=request.form['ranking'],
            review=request.form['review'],
            img_url=request.form['url']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


# Update
@app.route('/update', methods=['GET', 'POST'])
def update():
    form = UpdateForm()
    movie_id = request.args.get['id'],
    movie_to_update = Movies.query.get[movie_id],
    if form.validate_on_submit():
        movie_to_update.review = form.review.data,
        movie_to_update.rating = float(form.rating.data),
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie_to_update, form=form)


# Delete
@app.route('/delete')
def delete():
    # delete by id
    movie_id = request.args.get('id')
    movie_to_delete = Movies.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
