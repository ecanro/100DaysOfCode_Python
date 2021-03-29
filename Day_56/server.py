from flask import Flask, render_template

# init flask
app = Flask(__name__)

#main page
@app.route('/')
# @app.route('/index/<name>')
def main(name=None):
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)

