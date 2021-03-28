from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # flask accept html  and inline styles in the return
    return ('<h1 style="text-align:center">Hello, mundo!</h1>'\
            '<p>Lorem ipsum</p>'
            )

# using decorators for the styles
def make_bold(function):
    def wrapper():
        # return f'<b>{function()}</b>'
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

# but we can used a decorator with *args
def make_text_styles(*args):
    pass

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)