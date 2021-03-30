from flask import Flask, render_template
import requests, datetime
from post import Post

app = Flask(__name__)

current_year = datetime.datetime.now()
posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)
print(post_objects)

@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects, year=current_year.year)

#posts
@app.route('/post/<int:index>')
def show_post(index):
    request_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            request_post = blog_post
            print(request_post)
    return render_template('post.html', post=request_post, year=current_year.year)


if __name__ == "__main__":
    app.run(debug=True)
