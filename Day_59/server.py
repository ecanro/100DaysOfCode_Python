from flask import Flask, render_template, request
import datetime, requests

app = Flask(__name__)

current_year = datetime.datetime.now()


# index
@app.route('/')
def home():
    return render_template('index.html', year=current_year.year)


# login
@app.route('/login', methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"


@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    app.run(port=5000, debug=True)