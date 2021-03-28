from flask import Flask
import random

# Global var
#TODO: generate a random number between 0 and 100
random_number = random.randint(1, 100)
print(random_number)
# number of attempts
attempts = 10

# init flask
app = Flask(__name__)

#main page
@app.route('/')
def main():
    # flask accept html  and inline styles in the return
    return ('<h1 style="text-align:center; margin-top:50px">Guest a number between 1 and 100</h1>'\
            f'<h3 style="text-align:center">You have {attempts} attemps </h3>'\
            '<p style="text-align:center">Insert the number in the url after the /"you number"'
            '<img style="display:block;margin-left:auto; margin-right:auto; width:20%" src="https://media.giphy.com/media/UDU4oUJIHDJgQ/giphy.gif" alt="count numbers">'
            )


# simple url input number and checking and load the page
@app.route('/<guess>')
def number(guess):
    global attempts
    while attempts > 0:
        attempts -= 1
        if guess.isalpha():
            you_are = "You must enter a number !!! "
            image = "https://media.giphy.com/media/SACoDGYTvVNhZYNb5a/giphy.gif"
            color = "blue"
        elif int(guess) < 1 or int(guess) > 100:
            you_are = "Out of the range !!!"
            image = "https://media.giphy.com/media/SACoDGYTvVNhZYNb5a/giphy.gif"
            color = "red"
        elif int(guess) > random_number:
            you_are = "Too High, try again ! !!!"
            image = "https://media.giphy.com/media/3o7TKHVU0xsgGDCyPu/giphy.gif"
            color = "green"
        elif int(guess) < random_number :
            you_are = "Too Low, try again !"
            image = "https://media.giphy.com/media/ky9vnG678kzD91TO3N/giphy.gif"
            color = "green"
        else:
            you_are = "You found me!"
            image = "https://media.giphy.com/media/Od0QRnzwRBYmDU3eEO/giphy.gif"
            color = "brown"
        return (f'<h2 style="color: {color}; text-align: center">{you_are}</h2>' \
                f'<h3 style="text-align:center">You have {attempts} attemps </h3>' \
                f'<img style="display:block;margin-left:auto; margin-right:auto; width:20%" src={image}>'
                )


if __name__ == "__main__":
    app.run(debug=True)







high = "https://media.giphy.com/media/ky9vnG678kzD91TO3N/giphy.gif"

low = "https://media.giphy.com/media/dsQvwwzZq4SMm8ZIyi/giphy.gif"

