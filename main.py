import json   # ugrađeni moduli

from flask import Flask  # moduli instalirani preko pipa
from flask.json import jsonify

from dataset import get_country_data # naši moduli



app = Flask(__name__)  # Flask("main.py")


@app.route("/api")
def country_data():
    data_df = get_country_data()
    data_dict = json.loads(data_df.to_json())
    return jsonify(data_dict)

@app.route("/api/<country>")
def country_specific_data(country):
    data_df = get_country_data()
    data_dict = json.loads(data_df.to_json())

    country_dict = data_dict.get(country.lower(), {})

    return jsonify(country_dict)






# dict_primjer = {
#     "Ime": "Marko",
#     "Prezime": "Markic",
#     "Email": "marko@mail.com"
# }


# @app.route("/")
# def home():
#     return "<h1><a href='/about'>Home page</a></h1>"


# @app.route("/about")
# def about_page():
#     return "<p>About page</p>"


# @app.route("/user/<username>")
# def user(username):
#     return f"<h3>User page for {username}</h3>"


# @app.route("/json")
# def json():
#     return jsonify(dict_primjer)


# @app.route("/json/<key>")
# def json_value(key):
#     return dict_primjer.get(key, "Unknown key")