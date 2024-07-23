from flask import Flask


app = Flask(__name__) # Flask("main.py")


@app.route("/")
def home():
    return "<h1><a href='/about'>Home page</a></h1>"


@app.route("/about")
def about_page():
    return "<p>About page</p>"

@app.route("/user/<username>")
def user(username):
    return f"<h3>User page for {username}</h3>"