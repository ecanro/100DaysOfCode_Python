from flask import Flask, render_template
import random, datetime

#init flask
app = Flask(__name__)

#main page
@app.route('/')
def main():
    random_num = random.randint(0,10)
    current_year = datetime.datetime.now()

    return  render_template('index.html', a_variable=random_num, year=current_year.year)

if __name__ == "__main__":
    app.run(debug=True, port=3000)

