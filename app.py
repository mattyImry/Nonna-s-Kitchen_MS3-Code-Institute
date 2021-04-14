import os
import math
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, pymongo
from flask_paginate import get_page_args
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

    # idea & code for pagination  taken from
    # https://github.com/Sean-Mc-Mahon/McTasticRecipes
    # pagination

    recipes_per_page = 4
    current_page = int(request.args.get('current_page', 1))
    recipes = mongo.db.recipes.find().skip(
        (current_page - 1)*recipes_per_page).sort(
            '_id', pymongo.DESCENDING).skip(
                (current_page - 1)*recipes_per_page).limit(recipes_per_page)
    number_recipes = recipes.count()
    pages = range(1, int(math.ceil(number_recipes / recipes_per_page)) + 1)

    return render_template(
        "index.html", recipes=recipes,
        current_page=current_page, pages=pages,
        recipes_per_page=recipes_per_page,
        number_recipes=number_recipes)


# SEARCH FUNCTIONALITY
@app.route("/search", methods=["GET", "POST"])
def search():

    # idea & code for pagination  taken from
    # https://github.com/Sean-Mc-Mahon/McTasticRecipes
    # pagination

    recipes_per_page = 4
    current_page = int(request.args.get('current_page', 1))
    recipes = mongo.db.recipes.find().skip(
        (current_page - 1)*recipes_per_page).sort(
            '_id', pymongo.DESCENDING).skip(
                (current_page - 1)*recipes_per_page).limit(recipes_per_page)
    number_recipes = recipes.count()
    pages = range(1, int(math.ceil(number_recipes / recipes_per_page)) + 1)
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))

    return render_template(
        "index.html", recipes=recipes,
        current_page=current_page, pages=pages,
        recipes_per_page=recipes_per_page,
        number_recipes=number_recipes)


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
        return redirect(url_for("myprofile", username=session["user"]))

    return render_template("register.html")


# LOGIN PAGE
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
                return redirect(url_for(
                        "myprofile", username=session["user"]))
            else:
                # password no matched
                flash("Incorrect Username or password")
                return redirect(url_for("login"))

        else:
            # user no matched
            flash("Incorrect Username/password")
            return redirect(url_for("login"))

    return render_template("login.html")


# PROFILE'S USER PAGE
@app.route("/myprofile/<username>", methods=["GET", "POST"])
def myprofile(username):
    # session user's username form database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    recipes_per_page = 4
    current_page = int(request.args.get('current_page', 1))
    recipes = mongo.db.recipes.find().skip(
        (current_page - 1)*recipes_per_page).sort(
            '_id', pymongo.DESCENDING).skip(
                (current_page - 1)*recipes_per_page).limit(recipes_per_page)
    number_recipes = recipes.count()
    pages = range(1, int(math.ceil(number_recipes / recipes_per_page)) + 1)

    # display user and number of recipes for the current user
    # recipes = mongo.db.recipes.find()
    user_number_of_recipes = mongo.db.recipes.count({"author": username})

    if session["user"]:
        return render_template(
            "myprofile.html", username=username,
            user_number_of_recipes=user_number_of_recipes,
            recipes=recipes, current_page=current_page,
            pages=pages, number_recipes=number_recipes,
            recipes_per_page=recipes_per_page)

    return redirect(url_for("login"))


# DELETE PROFILE'S USER AND USER'S RECIPES
@app.route("/delete_user/<username>")
def delete_user(username):
    mongo.db.users.remove({"username": username})
    mongo.db.recipes.remove({"author": username})
    flash("Profile removed succesfully")

    # delete user from session cookie.
    session.pop("user")
    return redirect(url_for("index"))


# LOG OUT LINK WILL REDIRECT THE USER TO HOME PAGE
@app.route("/logout")
def logout():
    flash("You are now logged out")

    # delete user from session cookie.
    session.pop("user")
    return redirect(url_for("index"))


# ADD RECIPE TO DATABASE
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():

    if request.method == "POST":

        # help from tutor team to write code
        # for splittin ingredients and preparetion

        ingredients = request.form.get("ingredients").split(",")
        preparation = request.form.get("preparation").split(".")
        recipe = {
            "type": request.form.get("type"),
            "recipe_name": request.form.get("recipe_name"),
            "difficulty": request.form.get("difficulty"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serving": request.form.get("serving"),
            "ingredients": ingredients,
            "preparation": preparation,
            "is_vegetarian": request.form.get("is_vegetarian"),
            "author": session["user"],
            "image": request.form.get("image")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added Succesfully!")
        return redirect(url_for("index"))

    return render_template("add_recipe.html")


# UPDATE RECIPE TO DATABASE
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):

    if request.method == "POST":

        # help from tutor team to write code
        # for splittin ingredients and preparetion

        ingredients = request.form.get("ingredients").split(",")
        preparation = request.form.get("preparation").split(".")

        submit = {
            "type": request.form.get("type"),
            "recipe_name": request.form.get("recipe_name"),
            "difficulty": request.form.get("difficulty"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serving": request.form.get("serving"),
            "ingredients": ingredients,
            "preparation": preparation,
            "is_vegetarian": request.form.get("is_vegetarian"),
            "author": session["user"],
            "image": request.form.get("image")
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        username = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})["author"]

        flash("Recipe Succesfully Updated!")
        return render_template(
            "single_recipe.html", recipe=recipe, username=username)

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


# DELETE RECIPE FROM DATABASE
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted succesfully!")
    return redirect(url_for("index"))


# SINGLE RECIPE SHOWN WHEN CLICKING THE RECIPE CARD FROM INDEX PAGE
    # CODE TAKEN FROM
    # https://github.com/Sean-Mc-Mahon/McTasticRecipes

@app.route("/single_recipe/<recipe_id>")
def single_recipe(recipe_id):

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    username = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})["author"]
    return render_template(
        "single_recipe.html", recipe=recipe, username=username,)


# 404 ERROR NOT FOUND
@app.errorhandler(404)
def error_handler_404(error):
    return render_template("404.html"), 404


# 500 INTERNAL SERVER ERROR
@app.errorhandler(500)
def error_handler_500(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
