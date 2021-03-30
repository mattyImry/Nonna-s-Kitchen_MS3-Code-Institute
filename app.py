import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# CONFIGURATION

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# HOME PAGE
@app.route("/")
@app.route("/index")
def index():
    recipes = mongo.db.recipes.find()
    return render_template("index.html", recipes=recipes)


# REGISTER PAGE
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checking of users exist in database
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry Username already exist, try again")
            return render_template("register.html")

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Thank you! You are now registered")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exist in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if password match user
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                # if username and password match create session cookie
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome back {}".format(
                        request.form.get("username")))
            else:
                # password no matched
                flash("Incorrect Username or password")
                return redirect(url_for("login"))

        else:
            # user no matched
            flash("Incorrect Username/password")
            return redirect(url_for("login"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
