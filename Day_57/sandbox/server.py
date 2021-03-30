from flask import Flask, render_template
import random, datetime, requests

# Global var

AGIFY_EDNPOINT = "https://api.agify.io/?name="
GENDERIZE_ENPOINT = "https://api.genderize.io/?name="
# NATIONALIZE_EDNPOINT ="https://api.nationalize.io/?name="

#init flask
app = Flask(__name__)


# main page
@app.route('/')
def home():
    random_num = random.randint(0, 10)
    current_year = datetime.datetime.now()
    return render_template('index.html', a_variable=random_num, year=current_year.year)


# guess page
@app.route('/guess')
@app.route('/guess/<name>')
def guess(name=None):
    agify_response = requests.get(url=f'{AGIFY_EDNPOINT}{name}')
    age = agify_response.json()['age']
    genderize_response = requests.get(url=f'{GENDERIZE_ENPOINT}{name}')
    gender = genderize_response.json()['gender']
    current_year = datetime.datetime.now()
    return render_template('guess.html', my_name=name, age=age, gender=gender, year=current_year.year)

# blog page
@app.route('/blog/<id>')
def get_blog(id):
    API_ENPOINT = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(url=API_ENPOINT)
    all_blog_posts = response.json()
    print(all_blog_posts)
    # print(response.json()['title'])
    # print(response.json()['subtitle'])
    # print(response.json()['body'])
    return render_template('blog.html', posts=all_blog_posts)

# go to post
@app.route('/post')
def post():
    return render_template('post.html')


if __name__ == "__main__":
    app.run(debug=True, port=3000)