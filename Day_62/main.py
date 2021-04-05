from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
# import sqlite3
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
FILE_URI = 'sqlite:///new-books-collection.db'

## CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = FILE_URI
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create the database file and tables
# This code must come _after_ the class definition
if not os.path.isfile(FILE_URI):
    db.create_all()

# all_books = [
    # {
    #     "title": "Harry Potter",
    #     "author": "J. K. Rowling",
    #     "rating": 9/10,
    # }
# ]


# TODO: init the CRUD

# CREATE RECORD
# new_book = Book(id=1, title="The Lord of the Ring", author="J.R. Tolkiem", rating=9.5)
# db.session.add(new_book)
# db.session.commit()

# READ
# All records
# all_books = db.session.query(Book).all()

# Particular record
# book = Book.query.filter_by(title="The Lord of the Ring").first()

# UPDATE
# By Query
# book_to_update = Book.query.filter_by(title="The Lord of the Ring").first()
# book_to_update.title = "The Lord of the Ring Cap. 1"
# db.session.commit()

# By id(Primary Key)
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "The Lord of the Ring Cap. 1"
# db.session.commit()

# DELETE
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()


class Form(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = SelectField('Rating', choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    submit = SubmitField('Add Book')


@app.route('/')
def home():
    # Read
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = Form
    # Create
    if request.method == 'POST':
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating'],
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    # Update
    if request.method == 'POST':
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template('edit.html', book=book_selected)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')

    # Delete by id
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

