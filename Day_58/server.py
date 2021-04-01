from flask import Flask, render_template, request
import datetime, requests, smtplib, config
from post import Post


app = Flask(__name__)

MY_EMAIL = config.email
MY_PASSWORD = config.passw

current_year = datetime.datetime.now()

posts = requests.get("https://api.npoint.io/da11f716936ce423098d").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["date"], post["title"], post["posted"], post["subtitle"], post["body"])
    post_objects.append(post_obj)
#print(post_objects)


# home
@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects, year=current_year.year)


# about
@app.route('/about')
def about():
    return render_template('about.html', year=current_year.year)


# posts
@app.route('/post/<int:index>')
def show_post(index):
    request_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            request_post = blog_post
            print(request_post)
    return render_template('post.html', post=request_post, year=current_year.year)


# posts
@app.route('/contact')
def contact():
    return render_template('contact.html', year=current_year.year)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=email_message)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
